def on_up_pressed():
    if player1.vy == 0:
        player1.vy = -200
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_overlap_tile(sprite, location):
    info.set_score(score)
    game.game_over(False)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile
    """),
    on_overlap_tile)

def on_button_pressed():
    global arrow_count
    if controller.B.is_pressed():
        if controller.left.is_pressed():
            if controller.down.is_pressed():
                arrow_count = 999
controller.any_button.on_event(ControllerButtonEvent.PRESSED, on_button_pressed)

def on_a_pressed():
    global arrow, arrow_count
    if arrow_count != 0:
        if Facing == 1:
            arrow = sprites.create_projectile_from_sprite(img("""
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
                """),
                player1,
                arrow_speed_x,
                0)
            pause(200)
            arrow_count += -1
            info.set_score(arrow_count)
    if arrow_count != 0:
        if Facing == -1:
            arrow = sprites.create_projectile_from_sprite(img("""
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
                """),
                player1,
                arrow_speed_x,
                0)
            pause(200)
            arrow_count += -1
            info.set_score(arrow_count)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_left_pressed():
    global arrow_speed_x, Facing
    arrow_speed_x = -150
    Facing = -1
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_pressed():
    global arrow_speed_x, Facing
    arrow_speed_x = 150
    Facing = 1
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_life_zero():
    info.set_score(score)
    game.game_over(False)
info.on_life_zero(on_life_zero)

def on_on_destroyed(sprite2):
    global score, ghost
    score += 1
    ghost = sprites.create(img("""
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
    """),
        SpriteKind.enemy)
    ghost.follow(player1, 75)
    ghost.set_position(randint(0, 200), randint(0, 200))
sprites.on_destroyed(SpriteKind.enemy, on_on_destroyed)

def on_on_overlap(sprite3, otherSprite):
    sprites.destroy(sprite3)
    sprites.destroy(otherSprite)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite4, otherSprite2):
    info.change_life_by(-1)
    pause(1000)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

arrow_speed_x = 0
arrow: Sprite = None
Facing = 0
score = 0
arrow_count = 0
ghost: Sprite = None
player1: Sprite = None
scene.set_background_color(12)
tiles.set_current_tilemap(tilemap("""
    level2
"""))
player1 = sprites.create(img("""
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
    """),
    SpriteKind.player)
ghost = sprites.create(img("""
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
    """),
    SpriteKind.enemy)
ghost.set_position(randint(0, 200), randint(0, 200))
ghost.follow(player1, 75)
info.set_life(3)
arrow_count = 50
controller.move_sprite(player1, 100, 0)
scene.camera_follow_sprite(player1)
player1.ay = 350
info.set_score(arrow_count)
score = 0