const fs = require('fs');

const command = process.argv[2];
const name = process.argv[3];
const marks = process.argv[4];

// JSON file se data lo
function getData() {
  try {
    const data = fs.readFileSync('students.json', 'utf8');
    return JSON.parse(data);
  } catch (err) {
    return [];
  }
}

// JSON file mein data likho
function saveData(students) {
  fs.writeFileSync('students.json', JSON.stringify(students, null, 2));
}

// ADD
function addStudent() {
  const students = getData();
  const newStudent = { name: name, marks: marks };
  students.push(newStudent);
  saveData(students);
  console.log('Student Added:', newStudent);
}

// REMOVE
function removeStudent() {
  const students = getData();
  const updated = [];
  for (let i = 0; i < students.length; i++) {
    if (students[i].name !== name) {
      updated.push(students[i]);
    }
  }
  saveData(updated);
  console.log('Student Removed:', name);
}

// DISPLAY
function displayStudents() {
  const students = getData();
  if (students.length === 0) {
    console.log('No Students Found!');
  } else {
    for (let i = 0; i < students.length; i++) {
      console.log('Name:', students[i].name, '| Marks:', students[i].marks);
    }
  }
}

// Command check
if (command === 'add') {
  addStudent();
} else if (command === 'remove') {
  removeStudent();
} else if (command === 'display') {
  displayStudents();
} else {
  console.log('Invalid Command! Use: add / remove / display');
}