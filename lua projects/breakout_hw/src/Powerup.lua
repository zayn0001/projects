Powerup = Class{}

function Powerup:init(power)
    self.inPlay = false
    self.power = power
    self.width = 16
    self.height = 16
    self.x = math.random(8, VIRTUAL_WIDTH - 8)
    self.y = math.random(112, VIRTUAL_HEIGHT - 48)
    self.active = false
end

function Powerup:trigger(number)
    self.inPlay = math.random(number) == 1 and true or false
    self.x = math.random(8, VIRTUAL_WIDTH - 16)
    self.y = math.random(112, VIRTUAL_HEIGHT - 48)
end

function Powerup:render()
    if self.inPlay then
        love.graphics.draw(gTextures['main'], gFrames['powerups'][self.power], self.x, self.y)
    end
end

function Powerup:collides(ball)
    if self.x > ball.x + ball.width or ball.x > self.x + self.width then
        return false
    end
    if self.y > ball.y + ball.height or ball.y > self.y + self.height then
        return false
    end 
    return true
end