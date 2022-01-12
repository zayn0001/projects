PlayState = Class{__includes = BaseState}

PIPE_SPEED = 60
PIPE_WIDTH = 70
PIPE_HEIGHT = 288
PIPE_INTERVAL_SECS = math.random(3,4)
GAP_HEIGHT = math.random(80,100)

function PlayState:init()
    self.bird = Bird()
    self.pipePairs = {}
    self.timer = 0
    self.score = 0
    --self.minpos = -PIPE_HEIGHT + 50
    --self.maxpos = -PIPE_HEIGHT + VIRTUAL_HEIGHT - 50 - GAP_HEIGHT
    --self.lastY = -PIPE_HEIGHT + math.random(50, VIRTUAL_HEIGHT-50-GAP_HEIGHT) 
end

function PlayState:update(dt)

    self.timer = self.timer + dt

    if self.timer >= PIPE_INTERVAL_SECS then
        --local y = math.max(self.minpos, math.min(self.lastY + math.random(-30, 30), self.maxpos))
        --self.lastY = y
        --local y = -PIPE_HEIGHT + math.random(VIRTUAL_HEIGHT-50-GAP_HEIGHT) + 50
        PIPE_INTERVAL_SECS = math.random(3,4)
        GAP_HEIGHT = math.random(80,100)
        local y = -PIPE_HEIGHT + math.random(50, VIRTUAL_HEIGHT-50-GAP_HEIGHT)
        table.insert(self.pipePairs, PipePair(y))
        self.timer = 0
    end

    for k,pair in pairs(self.pipePairs) do
        if not pair.scored then
            if pair.x + PIPE_WIDTH < self.bird.x then
                self.score = self.score + 1
                pair.scored = true
                sounds['score']:play()
                print(pair.y)
            end
        end
        pair:update(dt)
    end

    for k, pair in pairs(self.pipePairs) do
        if pair.remove then
            table.remove(self.pipePairs, k)
        end
    end

    for k, pair in pairs(self.pipePairs) do
        for l, pipe in pairs(pair.pipes) do
            if self.bird:collides(pipe) then
                sounds['explosion']:play()
                sounds['hurt']:play()

                gStateMachine:change('score', self.score)
            end
        end
    end

    self.bird:update(dt)

    if self.bird.y > VIRTUAL_HEIGHT - 15 then
        sounds['explosion']:play()
        sounds['hurt']:play()

        gStateMachine:change('score',self.score)
    end

    if love.keyboard.wasPressed('p') then
        gStateMachine:change('pause', {
            ['pipePairs'] = self.pipePairs,
            ['bird'] = self.bird,
            ['timer'] = self.timer,
            ['score'] = self.score,
            ['lastY'] = self.lastY
        })
    end

end

function PlayState:render()
    for k, pair in pairs(self.pipePairs) do
        pair:render()
    end

    love.graphics.setFont(mediumFont)
    love.graphics.print('Score: ' ..tostring(self.score), 8, 8)

    self.bird:render()
end

function PlayState:enter(playStats)
    scrolling = true
    if playStats then
        self.bird = playStats['bird']
        self.pipePairs = playStats['pipePairs']
        self.timer = playStats['timer']
        self.score = playStats['score']
        self.lastY = playStats['lastY']
    end
end

function PlayState:exit()
    scrolling = false
end