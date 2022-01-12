--[[
    GD50
    Breakout Remake

    -- PlayState Class --

    Author: Colton Ogden
    cogden@cs50.harvard.edu

    Represents the state of the game in which we are actively playing;
    player should control the paddle, with the ball actively bouncing between
    the bricks, walls, and the paddle. If the ball goes below the paddle, then
    the player should lose one point of health and be taken either to the Game
    Over screen if at 0 health or the Serve screen otherwise.
]]

PlayState = Class{__includes = BaseState}

--[[
    We initialize what's in our PlayState via a state table that we pass between
    states as we go from playing to serving.
]]
function PlayState:enter(params)
    self.paddle = params.paddle
    self.bricks = params.bricks
    self.health = params.health
    self.score = params.score
    self.highScores = params.highScores
    self.level = params.level
    self.lockedbrick = params.lockedbrick
    self.recoverPoints = 5000
    self.growPoints = 500
    self.multiball = Powerup(9)
    self.key = Powerup(10)
    self.balls = params.balls
    self.lockedbrick = false
end

function PlayState:update(dt)

    for k,ball in pairs(self.balls) do
        ball:update(dt)
        self:paddlecollision(ball)
        self:brickcollision(ball)

        if ball.y >= VIRTUAL_HEIGHT then
            if #self.balls == 1 then
                self.health = self.health - 1
                self.paddle:shrink()
                gSounds['hurt']:play()

                if self.health == 0 then
                    gStateMachine:change('game-over', {
                    score = self.score,
                    highScores = self.highScores
                    })
                else
                    gStateMachine:change('serve', {
                    paddle = self.paddle,
                    bricks = self.bricks,
                    health = self.health,
                    score = self.score,
                    highScores = self.highScores,
                    level = self.level,
                    recoverPoints = self.recoverPoints,
                    growPoints = self.growPoints
                    })
                end
            else    
                table.remove(self.balls, k)
            end
        end
    end

    --powerup probability and occurence
    if self.multiball.inPlay == false then
        self.multiball:trigger(1000)
    end

    self.lockedbrick = false
    for k, brick in pairs(self.bricks) do
        if brick.color == 6 then
            self.lockedbrick = true
        end
    end
    if self.lockedbrick and self.key.inPlay == false and self.key.active == false then
        self.key:trigger(1000)
    end

    --powerup activation
    for k,ball in pairs(self.balls) do

        if self.multiball.inPlay and self.multiball:collides(ball) then
            self.balls[#self.balls+1] = Ball(ball.skin)
            self.balls[#self.balls].x = ball.x
            self.balls[#self.balls].y = ball.y 
            self.balls[#self.balls].dx = ball.dx -20
            self.balls[#self.balls].dy = ball.dy -20
            self.balls[#self.balls+1] = Ball(ball.skin)
            self.balls[#self.balls].x = ball.x
            self.balls[#self.balls].y = ball.y
            self.balls[#self.balls].dx = ball.dx + 20
            self.balls[#self.balls].dy = ball.dy + 20
            self.multiball.inPlay = false
            self.multiball.active = true
        end

        if self.key.inPlay and self.key:collides(ball) then
            self.key.inPlay = false
            self.key.active = true
        end
    end



    if self.paused then
        if love.keyboard.wasPressed('space') then
            self.paused = false
            gSounds['pause']:play()
        else
            return
        end
    elseif love.keyboard.wasPressed('space') then
        self.paused = true
        gSounds['pause']:play()
        return
    end

    -- update positions based on velocity
    self.paddle:update(dt)

    -- for rendering particle systems
    for k, brick in pairs(self.bricks) do
        brick:update(dt)
    end

    if love.keyboard.wasPressed('escape') then
        love.event.quit()
    end
end

function PlayState:render()

    for k,ball in pairs(self.balls) do
        ball:render()
    end

    -- render bricks
    for k, brick in pairs(self.bricks) do
        brick:render()
    end

    -- render all particle systems
    for k, brick in pairs(self.bricks) do
        brick:renderParticles()
    end

    self.multiball:render()
    self.paddle:render()
    self.key:render()

    renderScore(self.score)
    renderHealth(self.health)

    -- pause text, if paused
    if self.paused then
        love.graphics.setFont(gFonts['large'])
        love.graphics.printf("PAUSED", 0, VIRTUAL_HEIGHT / 2 - 16, VIRTUAL_WIDTH, 'center')
    end

end

function PlayState:checkVictory()
    for k, brick in pairs(self.bricks) do
        if brick.inPlay then
            return false
        end 
    end

    return true
end

function PlayState:paddlecollision(ball)
    if ball:collides(self.paddle) then
        
        ball.y = self.paddle.y - 8
        ball.dy = -ball.dy

        if ball.x < self.paddle.x + (self.paddle.width / 2) and self.paddle.dx < 0 then
            ball.dx = -50 + -(8 * (self.paddle.x + self.paddle.width / 2 - ball.x))
        
        elseif ball.x > self.paddle.x + (self.paddle.width / 2) and self.paddle.dx > 0 then
            ball.dx = 50 + (8 * math.abs(self.paddle.x + self.paddle.width / 2 - ball.x))
        end

        gSounds['paddle-hit']:play()
    end
end

function PlayState:brickcollision(ball)
    for k, brick in pairs(self.bricks) do

        if brick.inPlay and ball:collides(brick) then

            self.score = self.score + (brick.tier * 200 + brick.color * 25)

            --locked brick
            if brick.color == 6 then
                if self.key.active then
                    self.key.active = false
                    brick.color = 5
                    brick.tier = 0
                end
            else
                brick:hit()
            end

            
            if self.score > self.recoverPoints then
                self.health = math.min(3, self.health + 1)
                self.recoverPoints = math.min(100000, self.recoverPoints * 2)
                gSounds['recover']:play()
            end

            if self.score > self.growPoints then
                self.paddle:grow()
                self.growPoints = math.min(100000, self.growPoints * 2)
                gSounds['recover']:play()
            end

            if self:checkVictory() then
                gSounds['victory']:play()

                gStateMachine:change('victory', {
                    level = self.level,
                    paddle = self.paddle,
                    health = self.health,
                    score = self.score,
                    highScores = self.highScores,
                    balls = self.balls,
                    recoverPoints = self.recoverPoints
                })
            end

            
            if ball.x + 2 < brick.x and ball.dx > 0 then
                ball.dx = -ball.dx
                ball.x = brick.x - 8
            

            elseif ball.x + 6 > brick.x + brick.width and ball.dx < 0 then
                ball.dx = -ball.dx
                ball.x = brick.x + 32
            

            elseif ball.y < brick.y then
                ball.dy = -ball.dy
                ball.y = brick.y - 8
        
            else
                ball.dy = -ball.dy
                ball.y = brick.y + 16
            end

            if math.abs(ball.dy) < 150 then
                ball.dy = ball.dy * 1.02
            end

            break
        end
    end
end