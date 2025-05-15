import plotly.express as px
import pandas as pd
import requests
from geopy.distance import great_circle
import numpy as np

url = "https://services.swpc.noaa.gov/json/ovation_aurora_latest.json"
sigma = 1  # std dev for gaussian smoothing

my_loc = [44, -73]
# Get aurora data
data = requests.get(url)
auroras = pd.DataFrame(data.json())
auroras[['lon', 'lat', 'intensity']]  = pd.DataFrame(auroras["coordinates"].tolist(), index=auroras.index)
auroras["lon"] = auroras["lon"].apply(lambda x: x - 360 if x > 180 else x)
auroras = auroras.drop(columns=["Data Format", "coordinates", "type"])
# Calculate local intensity
auroras["distance"] = auroras.apply(lambda row: great_circle(my_loc, (row["lat"], row["lon"])).kilometers, axis=1)

# Gaussian weighting
weights = np.exp(-0.5 * (auroras["distance"] / (1000 * sigma)) ** 2)
weighted_sum = (auroras["intensity"] * weights).sum()
total_weight = weights.sum()
local_intensity = weighted_sum / total_weight if total_weight > 0 else 0
p_aurora = np.minimum(local_intensity / 4.5, 0.99) * 100


fig = px.density_map(
    auroras,
    lon=auroras["lon"],
    lat=auroras["lat"],
    z=auroras["intensity"],
    opacity=0.6,
    center=dict(lat=my_loc[0], lon=my_loc[1]),
    zoom=0,
)

# Update layout
fig.update_layout(
    title="NOAA Short Term Forecasted Aurora Intensity Map using OVATION Model",
    width = 750,
    height = 600
)


threshold = 10
import numpy as np
import plotly.graph_objects as go

# Generate a sample grid
lon = np.arange(-180, 181, 1)  # Longitude from -180 to 180
lat = np.arange(-90, 91, 1)    # Latitude from -90 to 90
data = np.random.rand(len(lat), len(lon))  # Example grid

# Normalize data for colormap (0 to 255)
from PIL import Image
import matplotlib.pyplot as plt

cmap = plt.get_cmap("viridis")  # Choose colormap
data_norm = (data - np.min(data)) / (np.max(data) - np.min(data))  # Normalize
img_rgba = (cmap(data_norm) * 255).astype(np.uint8)  # Convert to RGBA

# Create image overlay
image = Image.fromarray(img_rgba)

# Create a map with Mapbox
fig = go.Figure()

# Add the heatmap overlay as an image
fig.update_layout(
    mapbox=dict(
        style="open-street-map",  # Basemap style
        layers=[
            dict(
                source=image,  # Attach the generated image
                sourcetype="image",
                coordinates=[[-180, 90], [180, 90], [180, -90], [-180, -90]],  # Georeference corners
                opacity=0.5,  # Adjust transparency
            )
        ],
        center=dict(lat=0, lon=0),
        zoom=1,
    ),
    margin=dict(t=0, r=0, b=0, l=0),
)

fig.show()

if p_aurora > threshold:
    print("notify")
# Save to HTML to be used on GitHub Pages
# fig.write_html("assets/src/map2.html")
