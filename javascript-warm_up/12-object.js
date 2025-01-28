#!/usr/bin/node

const args = process.argv.slice(2).map(Number); // Convert arguments to integers

if (args.length < 2) {
  console.log(0);
} else {
  args.sort((a, b) => b - a); // Sort the array in descending order
  const index = args.indexOf(12); // Find the index of 12
  if (index !== -1) {
    args[index] = 89; // Replace 12 with 89
  }
  console.log(args[1]); // Print the second biggest integer
}
