//
//  ScrollpHAT.swift
//  sroll-phat-swift
//
//  Created by Fabio Ritrovato on 14/01/2016.
//  Copyright (c) 2016 orange in a day. All rights reserved.
//

public class ScrollpHAT {
    
    static private let i2cAddress: Int32 = 0x60
    static private let cmdSetMode: UInt8 = 0x00
    static private let cmdSetState: UInt8 = 0x01
    static private let cmdSetBrightness: UInt8 = 0x19
    static private let mode5x11: UInt8 = 0x03
    static private let font: [Int: [UInt8]] = [33: [23], 34: [3, 0, 3], 35: [10, 31, 10, 31, 10], 36: [2, 21, 31, 21, 8], 37: [9, 4, 18], 38: [10, 21, 10, 16], 39: [3], 40: [14, 17], 41: [17, 14], 42: [20, 14, 20], 43: [4, 14, 4], 44: [16, 8], 45: [4, 4], 46: [16], 47: [24, 6], 48: [14, 21, 14], 49: [18, 31, 16], 50: [25, 21, 18], 51: [17, 21, 10], 52: [14, 9, 28], 53: [23, 21, 9], 54: [14, 21, 8], 55: [25, 5, 3], 56: [10, 21, 10], 57: [2, 21, 14], 58: [10], 59: [16, 10], 60: [4, 10], 61: [10, 10, 10], 62: [10, 4], 63: [1, 21, 2], 64: [14, 29, 21, 14], 65: [30, 5, 30], 66: [31, 21, 10], 67: [14, 17, 17], 68: [31, 17, 14], 69: [31, 21, 17], 70: [31, 5, 1], 71: [14, 17, 29], 72: [31, 4, 31], 73: [17, 31, 17], 74: [9, 17, 15], 75: [31, 4, 27], 76: [31, 16, 16], 77: [31, 2, 4, 2, 31], 78: [31, 2, 12, 31], 79: [14, 17, 14], 80: [31, 9, 6], 81: [14, 17, 9, 22], 82: [31, 9, 22], 83: [18, 21, 9], 84: [1, 31, 1], 85: [15, 16, 16, 15], 86: [15, 16, 15], 87: [15, 16, 8, 16, 15], 88: [27, 4, 27], 89: [3, 28, 3], 90: [25, 21, 19], 91: [31, 17], 92: [6, 24], 93: [17, 31], 94: [2, 1, 2], 95: [16, 16, 16], 96: [1, 2], 97: [8, 20, 28], 98: [31, 20, 8], 99: [8, 20], 100: [8, 20, 31], 101: [14, 21, 2], 102: [30, 5], 103: [2, 21, 15], 104: [31, 4, 24], 105: [29], 106: [16, 13], 107: [31, 4, 26], 108: [31], 109: [28, 4, 24, 4, 24], 110: [28, 4, 24], 111: [8, 20, 8], 112: [30, 10, 4], 113: [4, 10, 30], 114: [28, 2], 115: [20, 10], 116: [15, 18], 117: [12, 16, 28], 118: [12, 16, 12], 119: [12, 16, 8, 16, 12], 120: [20, 8, 20], 121: [2, 20, 14], 122: [18, 26, 22], 123: [4, 14, 17], 124: [31], 125: [17, 14, 4], 126: [8, 4, 8, 4], 127: []]
    
    private let bus: SMBus
    private var buffer = [UInt8](repeating: UInt8(0x00), count: 11)
    private var offset = 0
    
    public init() throws {
        try bus = SMBus(busNumber: 1)
        try bus.writeI2CBlockData(address: ScrollpHAT.i2cAddress, command: ScrollpHAT.cmdSetMode, values: [ScrollpHAT.mode5x11])
        
    }
    
    public func update() throws {
        var window: [UInt8]
        if offset + 11 <= buffer.count {
            window = Array(buffer[offset..<offset + 11])
        } else {
            window = Array(buffer[offset..<buffer.count])
            window += Array(buffer.prefix(11 - window.count))
        }
        window.append(0xFF)
        try bus.writeI2CBlockData(address: ScrollpHAT.i2cAddress, command: ScrollpHAT.cmdSetState, values: window)
    }
    
    public func clear() throws {
        buffer = [UInt8](repeating: UInt8(0x00), count: 11)
        offset = 0
        try update()
    }
    
    public func setBrightness(_ brightness: Int) throws {
        try bus.writeI2CBlockData(address: ScrollpHAT.i2cAddress, command: ScrollpHAT.cmdSetBrightness, values: [UInt8(brightness)])
    }
    
    public func setColumn(x: Int, value: UInt8) {
        if buffer.count <= x {
            buffer += [UInt8](repeating: UInt8(0x00), count: x - buffer.count + 1)
        }
        buffer[x] = value
    }
    
    public func write(string: String, x: Int = 0) throws {
        var x = x
        for char in string.utf8 {
            if let fontChar = ScrollpHAT.font[Int(char)] {
                for c in fontChar {
                    setColumn(x: x, value: c)
                    x += 1
                }
            } else {
                setColumn(x: x, value: 0)
                x += 1
                setColumn(x: x, value: 0)
                x += 1
            }
            setColumn(x: x, value: 0)
            x += 1
        }
        try update()
    }
    
    public func setPixel(x: Int, y: Int, value: Bool) {
        guard x >= 0 && x < 11 && y >= 0 && y < 5 else { return }
        if value {
            buffer[x] |= UInt8(1 << y)
        } else {
            buffer[x] &= ~UInt8(1 << y)
        }
    }
    
    public func scroll() throws {
        try scroll(by: 1)
    }
    
    public func scroll(by: Int) throws {
        offset += by
        offset %= buffer.count
        try update()
    }
    
    public func scroll(to: Int = 0) throws {
        offset = to % buffer.count
        try update()
    }

}
