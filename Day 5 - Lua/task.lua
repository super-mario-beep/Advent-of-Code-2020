function readSeats()
    seats = {}
    counter = 0;
    while(true) do
        line = io.read("*l")
        if line == nil then
            break
        end
        seats[counter] = line
        counter = counter + 1
    end
    return seats;
end

function calculateSeatID(seat)
    rowEnd = 127
    rowStart = 0
    for i = 1, 7 do
        if seat:sub(i,i) == "B" then
            rowStart = math.floor((rowEnd+rowStart)/2)
        else 
            rowEnd = math.floor((rowStart+rowEnd)/2)
        end
    end
    
    seatEnd = 7
    seatStart = 0
    for i = 8, #seat do
        if seat:sub(i,i) == "R" then
            seatStart = math.floor((seatEnd+seatStart)/2)
        else 
            seatEnd = math.floor((seatStart+seatEnd)/2)
        end
    end
    return (rowEnd * 8) + seatEnd
end

local seats = readSeats()
local ids = {}
local id = 0

for i = 0, #seats do
    num = calculateSeatID(seats[i])
    ids[i] = num
    if id <= num  then
        id = num
    end
end

table.sort(ids)


for i = 0, #ids do
    if not ids[i] == i+32 then
        print(i+32)
        break
    end
end

print(id)


