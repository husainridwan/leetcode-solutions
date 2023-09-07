/**
 * @param {string[]} deadends
 * @param {string} target
 * @return {number}
 */
var openLock = function(deadends, target) {
    const dead = new Set(deadends);
    const visited = new Set();
    const queue = ['0000'];
    let level = 0;

    while (queue.length > 0) {
    const size = queue.length;

        for (let i = 0; i < size; i++) {
          const current = queue.shift();

          if (dead.has(current)) {
            continue;
          }
          if (current === target) {
            return level;
          }
          for (let j = 0; j < 4; j++) {
            const up = rotate(current, j, 1);
            const down = rotate(current, j, -1);

            if (!visited.has(up) && !dead.has(up)) {
              queue.push(up);
              visited.add(up);
            }

            if (!visited.has(down) && !dead.has(down)) {
              queue.push(down);
              visited.add(down);
            }
          }
        }
        level++;
        }
        return -1;
}

function rotate(code, wheel, direction) {
    const digits = code.split('');
    const currentDigit = parseInt(digits[wheel]);

    // Rotate the wheel in the specified direction
    let newDigit = (currentDigit + direction + 10) % 10;
    digits[wheel] = newDigit.toString();

    return digits.join('');
    }