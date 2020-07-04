// function main(input) {
//   const [counter, ...words] = input.split("\n");
//   for (let i = 0; i < parseInt(counter); i++) {
//     const a = words[i * 2].split("");
//     const b = words[i * 2 + 1].split("");
//     let deletions = 0;
//     count1 = new Array(26);
//     count1.fill(0);
//     count2 = new Array(26);
//     count2.fill(0);

//     a.forEach((e) => {
//       index = e.charCodeAt() - "a".charCodeAt();
//       count1[index] += 1;
//     });

//     b.forEach((e) => {
//       index = e.charCodeAt() - "a".charCodeAt();
//       count2[index] += 1;
//     });

//     deletions = 0;
//     for (let i = 0; i < 26; i++) {
//       deletions += Math.abs(count1[i] - count2[i]);
//     }
//     process.stdout.write(deletions + "\n");
//   }
// }

// process.stdin.resume();
// process.stdin.setEncoding("utf-8");

// let stdin_input = "";
// process.stdin.on("data", (c) => (stdin_input += c));
// process.stdin.on("end", () => main(stdin_input));

let head = {
  glasses: 1,
};

let table = {
  pen: 3,
  __proto__: head,
};

let bed = {
  sheet: 1,
  pillow: 2,
  __proto__: table,
};

let pockets = {
  money: 2000,
  __proto__: bed,
};

console.log(pockets.pen);
