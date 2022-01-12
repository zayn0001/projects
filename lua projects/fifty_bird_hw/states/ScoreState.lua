ScoreState = Class{__includes = BaseState}

function ScoreState:init()
end

function ScoreState:update(dt)
    if love.keyboard.wasPressed('enter') or love.keyboard.wasPressed('return') then
        gStateMachine:change('countdown')
    end
end

function ScoreState:render()

    love.graphics.setFont(flappyFont)
    love.graphics.printf('Oof! You lost!', 0, 64, VIRTUAL_WIDTH, 'center')

    love.graphics.setFont(mediumFont)
    love.graphics.printf('Score: ' .. tostring(self.score), 0, 100, VIRTUAL_WIDTH, 'center')
    
    if self.medal then
        love.graphics.draw(self.medal, VIRTUAL_WIDTH/2 - self.medal:getWidth()/2, 120)
    end

    love.graphics.printf('Press Enter to Play Again!', 0, 180, VIRTUAL_WIDTH, 'center')
end

function ScoreState:enter(score)
    self.score = score
    if self.score >= 15 then
        self.medal = love.graphics.newImage('images/gold.png')
    elseif self.score >= 10 then
        self.medal = love.graphics.newImage('images/silver.png')
    elseif self.score >= 5 then
        self.medal = love.graphics.newImage('images/bronze.png')
    end
end
