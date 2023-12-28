// HTML:
// Create a currency display element with id 'currency' in your HTML file

// CSS:
// Style the currency display element in your CSS file

// JavaScript:

// Get the canvas element and its 2D context
const canvas = document.getElementById('game-canvas');
const ctx = canvas.getContext('2d');

// Define game variables
const gameWidth = canvas.width;
const gameHeight = canvas.height;
const towerSize = 40;
const enemySize = 20;
const towerRange = 5000;
const projectileSpeed = 4;
const towerCost = 50; // Cost to buy a tower
// Define currency variable
let currency = 100; // Starting currency amount
// Update currency display
function updateCurrencyDisplay() {
  const currencyDisplay = document.getElementById('currency');
  currencyDisplay.textContent = currency;
}

// Define tower object
class Tower {
  constructor(x, y) {
    this.x = x;
    this.y = y;
    this.fireRate = 60; // Number of frames between shots
    this.fireCountdown = this.fireRate; // Countdown until next shot
    this.target = null; // Current target enemy
  }

  update() {
    this.fireCountdown--;

    if (this.fireCountdown <= 0) {
      this.fireCountdown = this.fireRate;

      // Find the nearest enemy within range
      const nearestEnemy = getNearestEnemy(this.x, this.y);
      if (nearestEnemy) {
        this.target = nearestEnemy;

        // Create a new projectile and add it to the projectiles array
        projectiles.push(
          new Projectile(this.x + towerSize / 2, this.y, nearestEnemy)
        );
      }
    }
  }

  draw() {
    ctx.fillStyle = 'blue';
    ctx.fillRect(this.x, this.y, towerSize, towerSize);
  }
}

// Define projectile object
class Projectile {
  constructor(x, y, targetEnemy) {
    this.x = x;
    this.y = y;
    this.speed = projectileSpeed;
    this.width = 6;
    this.height = 12;
    this.target = targetEnemy;
  }

  update() {
    const dx = this.target.x + enemySize / 2 - this.x;
    const dy = this.target.y + enemySize / 2 - this.y;
    const distance = Math.sqrt(dx * dx + dy * dy);
    const vx = (dx / distance) * this.speed;
    const vy = (dy / distance) * this.speed;
    this.x += vx;
    this.y += vy;
  }

  draw() {
    ctx.fillStyle = 'green';
    ctx.fillRect(this.x - this.width / 2, this.y, this.width, this.height);
  }
}

// Define enemy object
class Enemy {
  constructor(x, y) {
    this.x = x;
    this.y = y;
    this.speed = 1;
    this.health = 100;
  }

  update() {
    this.x += this.speed;
  }

  draw() {
    ctx.fillStyle = 'red';
    ctx.fillRect(this.x, this.y, enemySize, enemySize);
    ctx.fillStyle = 'green';
    ctx.fillRect(this.x, this.y - 10, (enemySize * this.health) / 100, 5);
  }
}

// Create an array to store towers
const towers = [];

// Create an array to store projectiles
const projectiles = [];

// Create an array to store enemies
const enemies = [];

// Function to calculate distance between two points
function calculateDistance(x1, y1, x2, y2) {
  const dx = x2 - x1;
  const dy = y2 - y1;
  return Math.sqrt(dx * dx + dy * dy);
}

// Function to get the nearest enemy within range of a tower
function getNearestEnemy(towerX, towerY) {
  let nearestEnemy = null;
  let minDistance = Infinity;

  enemies.forEach(function (enemy) {
    const distance = calculateDistance(
      towerX + towerSize / 2,
      towerY + towerSize / 2,
      enemy.x + enemySize / 2,
      enemy.y + enemySize / 2
    );

    if (distance <= towerRange && distance < minDistance) {
      nearestEnemy = enemy;
      minDistance = distance;
    }
  });

  return nearestEnemy;
}

// Event listener for mouse click
canvas.addEventListener('click', function (event) {
  const rect = canvas.getBoundingClientRect();
  const mouseX = event.clientX - rect.left;
  const mouseY = event.clientY - rect.top;

  // Check if the click was inside the game area and if the player has enough currency to buy a tower
  if (
    mouseX >= 0 &&
    mouseX <= gameWidth &&
    mouseY >= 0 &&
    mouseY <= gameHeight &&
    currency >= towerCost
  ) {
    // Calculate the grid position for tower placement
    const gridX = Math.floor(mouseX / towerSize) * towerSize;
    const gridY = Math.floor(mouseY / towerSize) * towerSize;

    // Create a new tower, deduct the cost from the currency, and add the tower to the towers array
    const newTower = new Tower(gridX, gridY);
    towers.push(newTower);
    currency -= towerCost;

    // Update the currency display
    updateCurrencyDisplay();
  }
});

// Game loop
function gameLoop() {
  // Clear the canvas
  ctx.clearRect(0, 0, gameWidth, gameHeight);

  // Update and draw towers
  towers.forEach(function (tower) {
    tower.update();
    tower.draw();
  });

  // Update and draw projectiles
  projectiles.forEach(function (projectile) {
    projectile.update();
    projectile.draw();
  });

  // Update and draw enemies
  enemies.forEach(function (enemy) {
    enemy.update();
    enemy.draw();
  });

  // Check for collision between projectiles and enemies
  projectiles.forEach(function (projectile) {
    if (
      calculateDistance(
        projectile.x,
        projectile.y,
        projectile.target.x + enemySize / 2,
        projectile.target.y + enemySize / 2
      ) < projectileSpeed
    ) {
      projectile.target.health -= 20; // Decrease enemy health when hit

      // Remove projectile if it hits an enemy
      projectiles.splice(projectiles.indexOf(projectile), 1);

      // Remove enemy if its health reaches zero or below
      if (projectile.target.health <= 0) {
        enemies.splice(enemies.indexOf(projectile.target), 1);
      }
    }
  });

  requestAnimationFrame(gameLoop);
}

// Function to spawn enemies at regular intervals
function spawnEnemy() {
  const startX = -enemySize; // Start enemies off-screen
  const startY = Math.random() * gameHeight; // Random vertical position

  enemies.push(new Enemy(startX, startY));

  // Increase the currency amount when an enemy is killed
  currency += 10; // Adjust the currency gained as desired

  // Call the function recursively to spawn enemies continuously
  setTimeout(spawnEnemy, 2000);
}

// Start the game loop
gameLoop();

// Start spawning enemies
spawnEnemy();

// Update the currency display initially
updateCurrencyDisplay();