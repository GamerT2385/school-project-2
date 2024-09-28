controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    if (player1.vy == 0) {
        player1.vy = -200
    }
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite3, otherSprite) {
    sprites.destroy(sprite3)
    sprites.destroy(otherSprite)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile`, function (sprite, location) {
    info.setScore(score)
    game.gameOver(false)
})
controller.anyButton.onEvent(ControllerButtonEvent.Pressed, function () {
    if (controller.B.isPressed()) {
        if (controller.left.isPressed()) {
            if (controller.down.isPressed()) {
                arrow_count = 999
            }
        }
    }
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (arrow_count != 0) {
        if (Facing == 1) {
            arrow = sprites.createProjectileFromSprite(img`
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                1 . . . . . . . . . . . . . . . 
                . 1 . . . . . . . . . . . . . . 
                1 . 1 . . . . . . . . . . . . . 
                . 1 . 1 . . . . . . . . . 9 . . 
                e e e e e e e e e e e e e 9 9 . 
                e e e e e e e e e e e e e 9 9 . 
                . 1 . 1 . . . . . . . . . 9 . . 
                1 . 1 . . . . . . . . . . . . . 
                . 1 . . . . . . . . . . . . . . 
                1 . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                `, player1, arrow_speed_x, 0)
            pause(200)
            arrow_count += -1
            info.setScore(arrow_count)
        }
    }
    if (arrow_count != 0) {
        if (Facing == -1) {
            arrow = sprites.createProjectileFromSprite(img`
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . 1 
                . . . . . . . . . . . . . . 1 . 
                . . . . . . . . . . . . . 1 . 1 
                . . 9 . . . . . . . . . 1 . 1 . 
                . 9 9 e e e e e e e e e e e e e 
                . 9 9 e e e e e e e e e e e e e 
                . . 9 . . . . . . . . . 1 . 1 . 
                . . . . . . . . . . . . . 1 . 1 
                . . . . . . . . . . . . . . 1 . 
                . . . . . . . . . . . . . . . 1 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                `, player1, arrow_speed_x, 0)
            pause(200)
            arrow_count += -1
            info.setScore(arrow_count)
        }
    }
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    arrow_speed_x = -150
    Facing = -1
})
sprites.onDestroyed(SpriteKind.Enemy, function (sprite2) {
    score += 1
    ghost = sprites.create(img`
        ........................
        ........................
        ........................
        ........................
        ..........ffff..........
        ........ff1111ff........
        .......fb111111bf.......
        .......f11111111f.......
        ......fd11111111df......
        ......fd11111111df......
        ......fddd1111dddf......
        ......fbdbfddfbdbf......
        ......fcdcf11fcdcf......
        .......fb111111bf.......
        ......fffcdb1bdffff.....
        ....fc111cbfbfc111cf....
        ....f1b1b1ffff1b1b1f....
        ....fbfbffffffbfbfbf....
        .........ffffff.........
        ...........fff..........
        ........................
        ........................
        ........................
        ........................
        `, SpriteKind.Enemy)
    ghost.follow(player1, 75)
    ghost.setPosition(randint(0, 200), randint(0, 200))
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite4, otherSprite2) {
    info.changeLifeBy(-1)
    pause(1000)
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    arrow_speed_x = 150
    Facing = 1
})
info.onLifeZero(function () {
    info.setScore(score)
    game.gameOver(false)
})
let arrow_speed_x = 0
let arrow: Sprite = null
let Facing = 0
let score = 0
let arrow_count = 0
let ghost: Sprite = null
let player1: Sprite = null
scene.setBackgroundColor(12)
tiles.setCurrentTilemap(tilemap`level2`)
player1 = sprites.create(img`
    . . . . . . . . . . . . . . . . 
    . . . . f f f f f f . . . . . . 
    . . . f 2 f e e e e f f . . . . 
    . . f 2 2 2 f e e e e f f . . . 
    . . f e e e e f f e e e f . . . 
    . f e 2 2 2 2 e e f f f f . . . 
    . f 2 e f f f f 2 2 2 e f . . . 
    . f f f e e e f f f f f f f . . 
    . f e e 4 4 f b e 4 4 e f f . . 
    . . f e d d f 1 4 d 4 e e f . . 
    . . . f d d d e e e e e f . . . 
    . . . f e 4 e d d 4 f . . . . . 
    . . . f 2 2 e d d e f . . . . . 
    . . f f 5 5 f e e f f f . . . . 
    . . f f f f f f f f f f . . . . 
    . . . f f f . . . f f . . . . . 
    `, SpriteKind.Player)
ghost = sprites.create(img`
    ........................
    ........................
    ........................
    ........................
    ..........ffff..........
    ........ff1111ff........
    .......fb111111bf.......
    .......f11111111f.......
    ......fd11111111df......
    ......fd11111111df......
    ......fddd1111dddf......
    ......fbdbfddfbdbf......
    ......fcdcf11fcdcf......
    .......fb111111bf.......
    ......fffcdb1bdffff.....
    ....fc111cbfbfc111cf....
    ....f1b1b1ffff1b1b1f....
    ....fbfbffffffbfbfbf....
    .........ffffff.........
    ...........fff..........
    ........................
    ........................
    ........................
    ........................
    `, SpriteKind.Enemy)
ghost.setPosition(randint(0, 200), randint(0, 200))
ghost.follow(player1, 75)
info.setLife(3)
arrow_count = 50
controller.moveSprite(player1, 100, 0)
scene.cameraFollowSprite(player1)
player1.ay = 350
info.setScore(arrow_count)
score = 0
