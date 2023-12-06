const fs = require('fs');

const loadFile = (filePath) => {
    try {
        const rawFile = fs.readFileSync(filePath, 'utf8');
        return rawFile.split('\n');
    } catch (error) {
        console.log(error);
    };
    return '';
}

const formatData = (rawData) => {
    const output = [];
    for (const line of rawData) {
        const arr = line.split(' ').filter(el => el !== '');
        arr.shift()
        output.push(arr.map(Number))
    }

    return output;
}

const calculateNoOfWays = (data) => {
    const numberOfRaces = data[0].length;
    const timeLimits = data[0];
    const recordDistance = data[1];
    const noOfWays = [];

    for (let i = 0; i < numberOfRaces; i++) {
        const currentTimeLimit = timeLimits[i];
        const currentRecordDistance = recordDistance[i];
        let winningStrategies = 0;

        for (let j = 1; j < currentTimeLimit - 1; j++) {
            let distanceTravelled = 0;
            const speed = j;
            const time = currentTimeLimit - j;
            distanceTravelled = speed * time;
            if (distanceTravelled > currentRecordDistance) {
                winningStrategies += 1;
            };
        };

        noOfWays.push(winningStrategies);
    };

    return noOfWays;
}

const filePath = 'input.txt';
const rawData = loadFile(filePath);
const data = formatData(rawData);
const winningStrateigesForEach = calculateNoOfWays(data);

const multipleOfAll = winningStrateigesForEach.reduce((total, current) => total * current, 1);
console.log(multipleOfAll)