const crypto = require('crypto');

/**
 * Attempts to crack the MD5 hash of a 5-digit PIN.
 * @param {string} hash - The MD5 hash of the original 5-digit PIN.
 * @returns {string|null} - The original PIN if found, otherwise null.
 */
function crack(hash) {
    // Loop through all possible 5-digit PINs from 00000 to 99999
    for (let pin = 0; pin <= 99999; pin++) {
        // Convert the number to a 5-digit string with leading zeros
        const pinString = pin.toString().padStart(5, '0');
        
        // Compute the MD5 hash of the current PIN
        const computedHash = crypto.createHash('md5').update(pinString).digest('hex');
        
        // Check if the computed hash matches the target hash
        if (computedHash === hash) {
            return pinString; // Return the PIN if a match is found
        }
    }
    
    return null; // Return null if no matching PIN was found
}

// Example usage (you can replace the hash with your test case):
const exampleHash = '827ccb0eea8a706c4c34a16891f84e7b'; // This is the MD5 hash for "12345"
console.log(crack(exampleHash)); // Should output "12345"
