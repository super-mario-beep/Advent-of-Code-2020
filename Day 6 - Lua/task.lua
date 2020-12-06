function readInput()
    seats = {}
    counter = 0;
    while(true) do
        line = io.read("*l")
        if line == nil then
            break
        end
        if #line == 1 then
            seats[counter] = "---"
        else
            seats[counter] = line
        end
        counter = counter + 1
    end
    seats[#seats+1] = "-eof-"
    return seats;
end

function isInObj(letter,obj)
    if obj == nil then
        return false
    end
    --for i = 0, #obj do
        --if letter == obj[letter] then
            --print("ture")
           -- return true
        --end
    --end
    return true
end

local rows = readInput()
local answers = {}
ans_counter = 0
local l = 0
for i = 0,#rows do
    local v = rows[i]
    if string.match(v, "-eof-") then
        break;
    end
    if string.match(v, "---") then
        for i = 0,#answers do
            print(answers[i])
            if answers[k] == l then
                ans_counter = ans_counter +1
            end
        end
        l = 0
        answers = {}
    else
        l = l +1
        for i = 1, #v-1 do --every char
            if not isInObj(v:sub(i,i), answers[v:sub(i,i)]) then
                answers[v:sub(i,i)] = 1
            else
                answers[v:sub(i,i)] = 2
            end
        end
    end
    print(v)
end
print(ans_counter)