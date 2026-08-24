package main

import (
	"bytes"
	"fmt"
	"io"
	"os"
	"path"
	"slices"
	"strings"
)

func le(value []byte) int {
	n := 0

	for i, el := range value {
		n += (int(el) << (i * 8))
	}

	return n
}

func be(value []byte) int {
	n := 0

	for _, el := range value {
		n = n << 8
		n |= int(el)
	}

	return n
}

func ip(value []byte) string {
	res := []string{}

	for _, el := range value {
		res = append(res, fmt.Sprintf("%d", int(el)))
	}

	return strings.Join(res, ".")
}

const (
	PROTOCOL_POSITION = 9
	SYN               = 0x02
	ACK               = 0x10
	TCP_FLAGS_OFFSET  = 13
	TCP_PROTOCOL      = 0x06
)

func read(r io.Reader, n int) []byte {
	value := make([]byte, n)
	if _, err := r.Read(value); err != nil {
		panic("error trying to read value")
	}

	return value
}

func skip(r io.Seeker, n int64, whence int) {
	if _, err := r.Seek(n, whence); err != nil {
		panic("error trying to skip value")
	}
}

// *.pcap file structure
// [ 24 bytes of header ] . [ 16 bytes of first packet header ] . [ inclLen of bytes of first packet ] ... [ 16 bytes of the n packet header ] . [ inclLen of bytes of n packet ]
func main() {
	wd, err := os.Getwd()
	if err != nil {
		panic(err)
	}

	// logPath := path.Join(wd, "csprimer", "computer-systems", "synflood", "synflood.pcap")
	logPath := path.Join(wd, "synflood.pcap")
	data, err := os.ReadFile(logPath)
	if err != nil {
		panic(err.Error())
	}

	reader := bytes.NewReader(data)

	magicNumber := read(reader, 4)
	byteOrder := ""

	if slices.Equal(magicNumber, []byte{0xD4, 0xC3, 0xB2, 0xA1}) {
		byteOrder = "little"
	} else if slices.Equal(magicNumber, []byte{0xA1, 0xB2, 0xC3, 0xD4}) {
		byteOrder = "big"
	} else {
		panic("file is not a pcap")
	}

	fmt.Printf("Byte order: %s\n", byteOrder)

	skip(reader, 20, io.SeekStart)

	linkType := read(reader, 4)

	if linkType := le(linkType); linkType != 0 {
		panic("unsupported link type")
	}

	count := 0
	initiated := 0
	acknowleged := 0

	for reader.Len() > 0 {
		packetHeader := make([]byte, 16)
		if _, err := reader.Read(packetHeader); err != nil {
			panic("error trying to read packet header")
		}

		inclLen := le(packetHeader[8:12])
		bodyStart, err := reader.Seek(0, io.SeekCurrent)
		if err != nil {
			panic("error trying to read packet header")
		}

		loopbackHeader := read(reader, 4)
		if le(loopbackHeader) != 2 {
			panic("unsupported address family. only ipv4 is supported")
		}

		skip(reader, 9, io.SeekCurrent)

		protocol := read(reader, 1)
		if protocol[0] != TCP_PROTOCOL {
			panic("uknown protocol")
		}

		skip(reader, 2, io.SeekCurrent)

		ips := read(reader, 8)
		sourceIp := ip(ips[:4])
		destIp := ip(ips[4:])
		sourcePort := read(reader, 2)
		destPort := read(reader, 2)

		skip(reader, 9, io.SeekCurrent)

		tcpFlags := read(reader, 1)
		isSyn := tcpFlags[0]&SYN != 0
		isAck := tcpFlags[0]&ACK != 0

		if isSyn && !isAck {
			initiated++
		}

		if isSyn && isAck {
			acknowleged++
		}

		if _, err := reader.Seek(bodyStart+int64(inclLen), io.SeekStart); err != nil {
			panic("error reading ip header")
		}

		if isSyn && isAck {
			fmt.Printf("%s:%d -> %s:%d SYN&ACK\n", sourceIp, be(sourcePort), destIp, be(destPort))
		} else if isSyn && !isAck {
			fmt.Printf("%s:%d -> %s:%d SYN\n", sourceIp, be(sourcePort), destIp, be(destPort))
		}

		// total packets count
		count += 1
	}

	fmt.Println("Total packets:", count)
	fmt.Println("With", initiated, "connections")
	fmt.Println(acknowleged, "acknowledged")
	fmt.Printf("%.2f%% of connections acknowledged", float64(acknowleged)/float64(initiated)*100)
}
