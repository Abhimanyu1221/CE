// fileOperations.js — Complete Codejs
const fs = require('fs');

// 1. WRITE - file banao
fs.writeFile('Sample.txt', 'Hello! This is Sample file.', function(err) {
  if (err) {
    console.log('Write Error:', err);
  } else {
    console.log('File Written Successfully!');

    // 2. READ - file padho
    fs.readFile('Sample.txt', 'utf8', function(err, data) {
      if (err) {
        console.log('Read Error:', err);
      } else {
        console.log('File Content:', data);

        // 3. OPEN - file open karo
        fs.open('Sample.txt', 'r', function(err, fd) {
          if (err) {
            console.log('Open Error:', err);
          } else {
            console.log('File Opened! File Descriptor:', fd);

            // 4. DELETE - file hatao
            fs.unlink('Sample.txt', function(err) {
              if (err) {
                console.log('Delete Error:', err);
              } else {
                console.log('File Deleted Successfully!');
              }
            });
          }
        });
      }
    });
  }
});