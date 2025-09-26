const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const { Pool } = require('pg');
const path = require('path');

const app = express();
const port = 3000;

// Middleware
app.use(cors());
app.use(bodyParser.json());
app.use(express.static('.'));

// Database connection
const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
});

// Initialize database table
async function initializeDatabase() {
  try {
    await pool.query(`
      CREATE TABLE IF NOT EXISTS marketing_signups (
        id SERIAL PRIMARY KEY,
        contact_info VARCHAR(255) NOT NULL,
        signup_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
      )
    `);
    console.log('Database table initialized successfully');
  } catch (error) {
    console.error('Error initializing database:', error);
  }
}

// API endpoint to handle marketing signups
app.post('/api/signup', async (req, res) => {
  try {
    const { contact } = req.body;
    
    if (!contact || contact.trim() === '') {
      return res.status(400).json({ 
        success: false, 
        message: 'Email or phone number is required' 
      });
    }

    // Store the signup in database
    const query = 'INSERT INTO marketing_signups (contact_info) VALUES ($1) RETURNING *';
    const result = await pool.query(query, [contact.trim()]);
    
    console.log('New signup:', result.rows[0]);
    
    res.json({ 
      success: true, 
      message: 'Thank you for signing up! You\'ll receive updates soon.',
      data: result.rows[0]
    });
    
  } catch (error) {
    console.error('Error saving signup:', error);
    res.status(500).json({ 
      success: false, 
      message: 'Sorry, there was an error processing your signup. Please try again.' 
    });
  }
});

// API endpoint to view signups (for admin purposes)
app.get('/api/signups', async (req, res) => {
  try {
    const result = await pool.query('SELECT * FROM marketing_signups ORDER BY created_at DESC');
    res.json({ success: true, data: result.rows });
  } catch (error) {
    console.error('Error fetching signups:', error);
    res.status(500).json({ success: false, message: 'Error fetching data' });
  }
});

// Serve static files
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

// Initialize database and start server
initializeDatabase().then(() => {
  app.listen(port, '0.0.0.0', () => {
    console.log(`Marketing server running on http://0.0.0.0:${port}`);
  });
});