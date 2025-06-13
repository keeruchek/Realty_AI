# US Neighborhood Comparison Tool

A Streamlit-based web application that helps users compare any two locations in the United States based on education, real estate, demographics, and safety metrics.

## Features

- 📊 Compare any two US locations side by side
- 📚 Educational statistics and school ratings
- 🏠 Real estate market analysis
- 👥 Demographic information
- 🚓 Safety and crime statistics
- 🤖 AI Assistant for additional questions

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/us-neighborhood-comparison.git
cd us-neighborhood-comparison
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit app:
```bash
streamlit run streamlit_app.py
```

2. Open your web browser and navigate to the URL shown in your terminal (typically http://localhost:8501)

3. Enter any two US locations you want to compare (format: City, State - e.g., "Seattle, WA")

4. Click "Compare Locations" to see the detailed comparison

## Data Sources

The application uses various APIs to gather real-time data:
- Census Bureau API for demographic data
- School ratings and educational statistics
- Real estate market data
- FBI Crime Data API for safety statistics

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Streamlit for the amazing framework
- Various data providers and APIs
- Contributors and users of the application
