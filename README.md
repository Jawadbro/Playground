# Playground - AI-Powered Public Speaking Coach 🎤

An intelligent public speaking coach that analyzes your startup pitches and provides personalized feedback in the style of Steve Jobs. Upload your pitch audio, get detailed analysis, and receive coaching to improve your presentation skills.

## 🌟 Features

### Core Functionality
- **Audio Analysis**: Upload audio files of your pitch for comprehensive analysis
- **Steve Jobs-Style Coaching**: Get feedback channeling the legendary presenter's style and wisdom
- **Timestamp-Based Feedback**: Specific improvements with exact timestamps
- **Pitch Script Enhancement**: AI-powered script rewriting and improvement suggestions
- **Real-time Chat Interface**: Interactive coaching sessions with the AI coach
- **Speech Transcription**: Automatic transcription of your audio for detailed analysis

### Advanced Coaching Features
- **Startup Pitch Specialized**: Tailored specifically for startup founders and entrepreneurs
- **Word/Phrase Analysis**: Detailed feedback on specific words and phrases used
- **Presentation Flow**: Analysis of speech structure and narrative flow
- **Performance Tracking**: Conversation history maintained throughout coaching sessions
- **Personalized Recommendations**: Context-aware advice based on your specific pitch content

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Google AI API key (Gemini)
- ElevenLabs API key (optional, for voice features)
- Modern web browser

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Jawadbro/Playground.git
   cd Playground
   ```

2. **Install Python dependencies**
   ```bash
   pip install flask flask-cors google-generativeai elevenlabs python-dotenv
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   GOOGLE_API_KEY=your_google_gemini_api_key
   ELEVENLABS_API_KEY=your_elevenlabs_api_key
   ```

4. **Run the application**
   ```bash
   python run.py
   ```

5. **Access the app**
   Open `http://localhost:5000` in your browser

## 📁 Project Structure

```
Playground/
├── backend/
│   ├── app.py                 # Main Flask application
│   └── models/
│       └── PublicSpeakingCoach.py  # Core AI coaching logic
├── frontend/
│   ├── templates/
│   │   └── index.html         # Main web interface
│   └── static/                # CSS, JS, and assets
├── run.py                     # Application entry point
├── .env                       # Environment variables
└── README.md                  # This file
```

## 🎯 How It Works

### 1. Audio Analysis Pipeline
```python
# Upload audio file
POST /upload_audio
- Accepts audio files in various formats
- Saves temporarily for processing
- Uses Google Gemini for speech analysis
- Returns detailed timestamp-based feedback
```

### 2. AI Coaching Process
The system uses Google's Gemini AI model with a specialized prompt that:
- Channels Steve Jobs' presentation style and wisdom
- Provides specific, actionable feedback
- Includes timestamps for precise improvements
- Offers encouraging yet constructive criticism

### 3. Interactive Coaching
```python
# Send coaching messages
POST /send_message
- Maintains conversation context
- Integrates audio analysis results
- Provides personalized coaching advice
- Responds in Steve Jobs' characteristic style
```

## 🔧 API Endpoints

### Upload Audio for Analysis
```http
POST /upload_audio
Content-Type: multipart/form-data

Parameters:
- file: Audio file (mp3, wav, m4a, etc.)

Response:
{
  "analysis": "Detailed analysis with timestamps and specific feedback..."
}
```

### Send Message to Coach
```http
POST /send_message
Content-Type: application/json

Body:
{
  "user_message": "Your question or request",
  "audio_analysis": "Previous analysis results",
  "audio_transcript": "Transcribed speech text"
}

Response:
{
  "response": "Steve Jobs-style coaching response..."
}
```

### Get Script Enhancement
```http
POST /show_me_how
Content-Type: application/json

Body:
{
  "user_message": "Enhancement request",
  "audio_transcript": "Original speech transcript"
}

Response:
{
  "response": "Enhanced script with improvements..."
}
```

## 💡 Usage Examples

### Basic Pitch Analysis
1. **Record Your Pitch**: Create an audio recording of your startup pitch
2. **Upload**: Use the web interface to upload your audio file
3. **Get Analysis**: Receive detailed feedback with specific timestamps
4. **Chat with Coach**: Ask follow-up questions and get personalized advice

### Script Enhancement
1. **Upload Original Pitch**: Start with your current pitch recording
2. **Request Enhancement**: Ask the coach to "show me how" to improve
3. **Receive Rewrite**: Get an enhanced version of your script
4. **Practice & Iterate**: Record the new version and repeat the process

## 🎨 The Steve Jobs Coaching Style

The AI coach is programmed to embody Steve Jobs' presentation philosophy:

- **Simplicity**: "Simplicity is the ultimate sophistication"
- **Storytelling**: Focus on narrative and emotional connection
- **Confidence**: Project authority and belief in your product
- **Precision**: Every word matters, eliminate unnecessary content
- **Passion**: Show genuine excitement about your solution

### Sample Coaching Response
*"Your opening grabbed attention, but at 2:30 you lost momentum. Steve would say 'Get to the point faster.' Your product demo at 4:15 was solid - that's where your passion showed. But remember, as I always said, 'People don't know what they want until you show it to them.' Make that revelation moment stronger."*

## 🛠️ Technical Implementation

### AI Model Integration
- **Google Gemini 1.5 Flash**: Latest model for fast, accurate analysis
- **Context Awareness**: Maintains conversation history throughout sessions
- **Specialized Prompting**: Custom prompts for startup pitch analysis

### Audio Processing
- **Multiple Formats**: Supports common audio formats (mp3, wav, m4a, etc.)
- **Temporary Storage**: Files processed and removed automatically
- **Speech Recognition**: Built-in transcription capabilities

### Web Framework
- **Flask**: Lightweight Python web framework
- **CORS Enabled**: Cross-origin requests supported
- **RESTful API**: Clean API design for easy integration

## 🔐 Environment Setup

### Required API Keys

1. **Google AI API Key**
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key
   - Add to your `.env` file as `GOOGLE_API_KEY`

2. **ElevenLabs API Key** (Optional)
   - Sign up at [ElevenLabs](https://elevenlabs.io/)
   - Get your API key from dashboard
   - Add to your `.env` file as `ELEVENLABS_API_KEY`

### Environment Variables
```env
# Required
GOOGLE_API_KEY=your_google_gemini_api_key

# Optional (for voice features)
ELEVENLABS_API_KEY=your_elevenlabs_api_key
```

## 🚀 Deployment

### Local Development
```bash
python run.py
# App runs on http://localhost:5000
```

### Production Deployment

#### Using Gunicorn
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 run:app
```

#### Docker Deployment
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "run.py"]
```

#### Cloud Platforms
- **Heroku**: Add `Procfile` with `web: python run.py`
- **Railway**: Direct deployment from GitHub
- **Google Cloud Run**: Use provided Docker configuration

## 🧪 Testing Your Pitch

### Best Practices
- **Clear Audio**: Ensure good microphone quality for accurate analysis
- **Appropriate Length**: 2-10 minute pitches work best
- **Natural Delivery**: Speak as you would to real investors
- **Multiple Iterations**: Upload improved versions to track progress

### Common Feedback Areas
- **Opening Hook**: Does your first 30 seconds grab attention?
- **Problem Statement**: Is the pain point clear and relatable?
- **Solution Clarity**: Can listeners understand what you're building?
- **Market Opportunity**: Are you thinking big enough?
- **Traction Evidence**: Do you have proof of progress?
- **Call to Action**: What specific ask are you making?

## 📈 Coaching Insights

The AI coach provides feedback on:
- **Verbal Delivery**: Pace, pauses, emphasis, and clarity
- **Content Structure**: Logical flow and narrative arc
- **Specific Improvements**: Exact timestamps with actionable advice
- **Steve Jobs Wisdom**: Relevant quotes and principles applied to your pitch
- **Script Enhancement**: Rewritten versions of your pitch with improvements

## 🤝 Contributing

### Development Setup
1. Fork the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Set up environment variables
6. Run tests and start developing!

### Areas for Contribution
- **Frontend Enhancement**: Improve the web interface
- **Additional Coaching Styles**: Add other legendary speakers
- **Advanced Analytics**: More detailed speech metrics
- **Mobile Support**: React Native or responsive improvements
- **Language Support**: Multi-language coaching capabilities

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Google Gemini AI**: Powering the intelligent analysis
- **ElevenLabs**: Voice generation capabilities
- **Steve Jobs**: Inspiration for the coaching methodology
- **Flask Community**: Excellent web framework
- **Startup Community**: For feedback and testing

## 📞 Support & Contact

- **Issues**: [GitHub Issues](https://github.com/Jawadbro/Playground/issues)
- **Feature Requests**: [GitHub Discussions](https://github.com/Jawadbro/Playground/discussions)
- **Documentation**: This README and inline code comments

---

**"Your time is limited, so don't waste it living someone else's life. Have the courage to follow your heart and intuition."** - Steve Jobs

*Perfect your pitch. Change the world.*
