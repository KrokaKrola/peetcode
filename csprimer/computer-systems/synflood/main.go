package main

import (
	"fmt"
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
	PACKET_HEADER_OFFSET = 4
	PROTOCOL_POSITION    = 9
	SYN                  = 0x02
	ACK                  = 0x10
	TCP_FLAGS_OFFSET     = 13
	TCP_PROTOCOL         = 0x06
)

// *.pcap file structure
// [ 24 bytes of header ] . [ 16 bytes of first packet header ] . [ inclLen of bytes of first packet ] ... [ 16 bytes of the n packet header ] . [ inclLen of bytes of n packet ]
func main() {
	wd, err := os.Getwd()
	if err != nil {
		panic(err)
	}

	logPath := path.Join(wd, "csprimer", "computer-systems", "synflood", "synflood.pcap")
	data, err := os.ReadFile(logPath)
	if err != nil {
		panic(err.Error())
	}

	// reader := bytes.NewReader(data)

	magicNumber := data[:4]
	byteOrder := ""

	if slices.Equal(magicNumber, []byte{0xD4, 0xC3, 0xB2, 0xA1}) {
		byteOrder = "little"
	} else if slices.Equal(magicNumber, []byte{0xA1, 0xB2, 0xC3, 0xD4}) {
		byteOrder = "big"
	} else {
		panic("file is not a pcap")
	}

	fmt.Printf("Byte order: %s\n", byteOrder)

	if linkType := le(data[20:24]); linkType != 0 {
		panic("unsupported link type")
	}

	packetHeaderSize := 16
	offset := 24
	count := 0
	initiated := 0
	acknowleged := 0

	for offset < len(data) {
		if offset+packetHeaderSize > len(data) {
			panic("invalid structure of the packet header")
		}

		packetHeader := data[offset : offset+packetHeaderSize]
		inclLen := le(packetHeader[8:12])

		packet := data[offset+packetHeaderSize : offset+packetHeaderSize+inclLen]
		loopbackHeader := le(packet[:PACKET_HEADER_OFFSET])

		if loopbackHeader != 2 {
			panic("unsupported address family. only ipv4 is supported")
		}

		ihl := packet[PACKET_HEADER_OFFSET] & 0x0F
		tcpStart := PACKET_HEADER_OFFSET + ihl*4

		if protocol := packet[PROTOCOL_POSITION+PACKET_HEADER_OFFSET]; protocol != TCP_PROTOCOL {
			panic("uknown protocol")
		}

		const SOURCE_IP_POSITION = 12
		const DEST_IP_POSITION = 16
		sourceIp := ip(packet[PACKET_HEADER_OFFSET+SOURCE_IP_POSITION : PACKET_HEADER_OFFSET+SOURCE_IP_POSITION+4])
		destIp := ip(packet[PACKET_HEADER_OFFSET+DEST_IP_POSITION : PACKET_HEADER_OFFSET+DEST_IP_POSITION+4])

		fmt.Println("sourceIp", sourceIp, "destIp", destIp)

		tcpFlags := packet[tcpStart+TCP_FLAGS_OFFSET]

		isSyn := tcpFlags&SYN != 0
		isAck := tcpFlags&ACK != 0

		if tcpFlags != 0 && isSyn && !isAck {
			initiated++
		}

		if tcpFlags != 0 && isSyn && isAck {
			acknowleged++
		}

		offset += packetHeaderSize
		offset += inclLen

		// total packets count
		count += 1
	}

	fmt.Println("Total packets:", count)
	fmt.Println("With", initiated, "connections")
	fmt.Println(acknowleged, "acknowledged")
	fmt.Printf("%.2f%% of connections acknowledged", float64(acknowleged)/float64(initiated)*100)
}
