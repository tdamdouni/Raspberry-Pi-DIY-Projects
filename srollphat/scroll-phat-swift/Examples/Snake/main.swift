//
//  main.swift
//  sroll-phat-swift
//
//  Created by Fabio Ritrovato on 14/01/2016.
//  Copyright (c) 2016 orange in a day. All rights reserved.
//

import Glibc

do {
    let pHAT = try ScrollpHAT()
    try pHAT.setBrightness(2)
    var snake = [(x: 0, y: 0, dx: 1), (x: -1, y: 0, dx: 1), (x: -2, y: 0, dx: 1)]
    for i in 0..<62 {
        for point in snake {
            pHAT.setPixel(x: point.x, y: point.y, value: true)
        }
        try pHAT.update()
        usleep(50000)
        pHAT.setPixel(x: snake[2].x, y: snake[2].y, value: false)
        for (i, point) in snake.enumerated() {
            var point = point
            point.x += point.dx
            if (point.x < 0 && point.dx == -1) || (point.x > 10 && point.dx == 1) {
                point.y += 1
                point.dx = -point.dx
            }
            snake[i] = point
        }
    }
} catch let e as SMBusError {
    print(e)
}
