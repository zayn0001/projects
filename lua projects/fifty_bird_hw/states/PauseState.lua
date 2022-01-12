PauseState = Class{__includes = PlayState}

PAUSE_IMG = love.graphics.newImage('images/pause.png')


function PauseState:update()
    if love.keyboard.wasPressed('p') then
        gStateMachine:change('play', self.playStats)
    end
end

function PauseState:render()
    self.playStats['bird']:render()
    for k, pair in pairs(self.playStats['pipePairs']) do
        pair:render()
    end
    love.graphics.setFont(flappyFont)
    love.graphics.print('Score: ' ..tostring(self.playStats['score']), 8, 8)

    love.graphics.draw(PAUSE_IMG, VIRTUAL_WIDTH/2 - PAUSE_IMG:getWidth()/2, VIRTUAL_HEIGHT/2 - PAUSE_IMG:getHeight()/2)
end

function PauseState:enter(playStats)
    self.playStats = playStats
    scrolling = false
    sounds['pause']:play()
    sounds['music']:pause()
end

function PauseState:exit()
    scrolling = true
    sounds['pause']:play()
    sounds['music']:play()
end
