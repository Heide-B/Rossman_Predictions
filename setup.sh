mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"heidemlbalcera@gmail.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
[theme]\n\
primaryColor=\"#ffffff\"\n\
backgroundColor=\"#000000\"\n\
secondaryBackgroundColor=\"#d9dcde\"\n\
textColor=\"#ffffff\"\n\
font=\"sans serif\"\n
" > ~/.streamlit/config.toml
