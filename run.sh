DATE=`date +%Y-%m-%d`
if [ -e "./data/restaurants.json" ]
then
    mv ./data/restaurants.json "./data/${DATE}_restaurants.json"
fi
if [ -e "./data/geocoded_restaurants.json" ]
then
    mv ./data/geocoded_restaurants.json "./data/${DATE}_geocoded_restaurants.json"
fi
cd scrapy
scrapy crawl list -o ../data/restaurants.json -t json
cd ..
cd geocoding
python geocoding.py
cd ..
