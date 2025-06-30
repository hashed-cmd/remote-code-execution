from flask import Flask

app = Flask(__name__)

@app.route("/getscript")
def get_script():
    lua_script = """

local Players = game:GetService("Players")
local player = Players.LocalPlayer

if player.Name == "Mehtab1501" then
    local playerGui = player:WaitForChild("PlayerGui")

    local screenGui = Instance.new("ScreenGui")
    screenGui.Name = "GoodmorningPopup"
    screenGui.Parent = playerGui

    local textLabel = Instance.new("TextLabel")
    textLabel.Size = UDim2.new(0.4, 0, 0.1, 0)
    textLabel.Position = UDim2.new(0.3, 0, 0.45, 0)
    textLabel.Text = "can u see my text?"
    textLabel.TextSize = 36
    textLabel.Font = Enum.Font.SourceSansBold
    textLabel.BackgroundColor3 = Color3.fromRGB(255, 255, 255)
    textLabel.TextColor3 = Color3.fromRGB(0, 0, 0)
    textLabel.BackgroundTransparency = 0.1
    textLabel.Parent = screenGui

    local uiCorner = Instance.new("UICorner")
    uiCorner.CornerRadius = UDim.new(0, 12)
    uiCorner.Parent = textLabel

    task.delay(5, function()
        screenGui:Destroy()
    end)
end

"""
    return lua_script, 200, {"Content-Type": "text/plain"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)
