const fs = require('fs')

const readFile = (filePath) => {
    let data = [];
    try {
        const rawFile = fs.readFileSync(filePath, 'utf-8');
        const file = rawFile.split('\n')
        for (let line of file) {
            data.push(line.split());
        };
    } catch (e) {
        console.log(e);
    };

    return data;
};

const formatGalaxy = (map) => {
    const newMap = []

}
const filePath = 'example.txt';
const data = readFile(filePath);

console.log(data);