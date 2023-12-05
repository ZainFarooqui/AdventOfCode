const fs = require('fs');

const loadFile = (filePath) => {
    try {
        const rawFile = fs.readFileSync(filePath, 'utf8');
        return rawFile;
    } catch (error) {
        console.log(error);
    };
    return '';
}

const transformData = (rawData) => {
    const lines = rawData.split("\n");

    const transformedData = [];

    for (const line of lines) {
        try{
            const splitLine = line.split(":");
            const cardId = Number(splitLine[0].split(" ")[1]);
            let winningNumbers = splitLine[1].split("|")[0].trim().split(" ");
            let numbersDrawn = splitLine[1].split("|")[1].trim().split(" ");

            winningNumbers = winningNumbers.filter(el => el !== '');
            numbersDrawn = numbersDrawn.filter(el => el !== '')
            const newCard = {
                cardId,
                winningNumbers,
                numbersDrawn,
                instances: 1
            };
            transformedData.push(newCard);
        } catch (error) {
            console.log(error);
        };
    };

    return transformedData;
}

const getNumberOfMatches = (winningNumbers, numbersDrawn) => {
    let matches = 0;
    const winningSet = new Set(winningNumbers);

    for (const number of numbersDrawn) {
        if (winningSet.has(number)) {
            matches++;
        };
    };

    return matches;
};

const getTotalPoints = (allCards) => {
    let totalPoints = 0;

    for (const card of allCards) {
        const {
            winningNumbers,
            numbersDrawn
        } = card;
        const winners = getNumberOfMatches(winningNumbers, numbersDrawn);
        if (winners > 0) {
            totalPoints += Math.pow(2, winners - 1);
        }
    }

    return totalPoints;
};

const applyScratchcardRules = (allCards) => {
    const numberOfCards = allCards.length;
    let numberOfScratchcards = 0;

    for (let i = 0; i < numberOfCards; i++) {
        const card = allCards[i];
        const {
            winningNumbers,
            numbersDrawn,
            instances
        } = card;
        numberOfScratchcards += instances;
        let matches = getNumberOfMatches(winningNumbers, numbersDrawn);
        let curr = i + 1;
        while (matches > 0 && i + matches < numberOfCards)  {
            allCards[curr].instances += instances;
            matches -= 1;
            curr += 1;
        };
    };

    return numberOfScratchcards;
};

const filePath = 'input.txt';
const data = loadFile(filePath);
const allCards = transformData(data);

const totalPoints = getTotalPoints(allCards);
const trueScore = applyScratchcardRules(allCards);

console.log('The total points for part one: ' + totalPoints);
console.log('The number of scratchcards in part two: ' + trueScore)