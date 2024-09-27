import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st
import altair as alt
import os
import geopandas as gpd
#from mplcursors import cursor
import warnings
warnings.filterwarnings('ignore')
# from pandasai import Agent
os.environ["PANDASAI_API_KEY"] = "$2a$10$V2z.cVTBim/PDwCesS"
st.set_page_config(page_title="Diabetes Analysis Dashboard", page_icon=":bar_chart:", layout="wide")
st.title(":bar_chart: Diabetes Analysis Dashboard")
st.markdown('<style> div.block-container{padding-top:2rem;}<style>',unsafe_allow_html=True)
st.page_icon="🏂"
alt.themes.enable("dark")

@st.cache_data
def get_data():
    final_data= pd.read_csv("data_with_regions.csv",encoding="ISO-8859-1")
    final_data['Number'] = pd.to_numeric(final_data['Number'])
    return final_data
#  
# # Define the region mapping as a dictionary
# region_mapping = {
#     "NHS Airedale, Wharfdale and Craven CCG": "Yorkshire and the Humber",
#     "NHS Ashford CCG": "South East England",
#     "NHS Aylesbury Vale CCG": "South East England",
#     "NHS Barking and Dagenham CCG": "London",
#     "NHS Barnet CCG": "London",
#     "NHS Barnsley CCG": "Yorkshire and the Humber",
#     "NHS Basildon and Brentwood CCG": "East of England",
#     "NHS Bassetlaw CCG": "Yorkshire and the Humber",
#     "NHS Bath and North East Somerset CCG": "South West England",
#     "NHS Bedfordshire CCG": "East of England",
#     "NHS Bexley CCG": "London",
#     "NHS Birmingham Cross city CCG": "West Midlands",
#     "NHS Birmingham South and Central CCG": "West Midlands",
#     "NHS Blackburn with Darwen CCG": "North West England",
#     "NHS Blackpool CCG": "North West England",
#     "NHS Bolton CCG": "North West England",
#     "NHS Bracknell and Ascot CCG": "South East England",
#     "NHS Bradford City CCG": "Yorkshire and the Humber",
#     "NHS Bradford Districts CCG": "Yorkshire and the Humber",
#     "NHS Brent CCG": "London",
#     "NHS Brighton and Hove CCG": "South East England",
#     "NHS Bristol CCG": "South West England",
#     "NHS Bromley CCG": "London",
#     "NHS Bury CCG": "North West England",
#     "NHS Calderdale CCG": "Yorkshire and the Humber",
#     "NHS Cambridgeshire and Peterborough CCG": "East of England",
#     "NHS Camden CCG": "London",
#     "NHS Cannock Chase CCG": "West Midlands",
#     "NHS Canterbury and Coastal CCG": "South East England",
#     "NHS Castle Point and Rochford CCG": "East of England",
#     "NHS Central London (Westminster) CCG": "London",
#     "NHS Central Manchester CCG": "North West England",
#     "NHS Chiltern CCG": "South East England",
#     "NHS Chorley and South Ribble CCG": "North West England",
#     "NHS City and Hackney CCG": "London",
#     "NHS Coastal West Sussex CCG": "South East England",
#     "NHS Corby CCG": "East Midlands",
#     "NHS Coventry and Rugby CCG": "West Midlands",
#     "NHS Crawley CCG": "South East England",
#     "NHS Croydon CCG": "London",
#     "NHS Cumbria CCG": "North West England",
#     "NHS Darlington CCG": "North East England",
#     "NHS Dartford, Gravesham and Swanley CCG": "South East England",
#     "NHS Doncaster CCG": "Yorkshire and the Humber",
#     "NHS Dorset CCG": "South West England",
#     "NHS Dudley CCG": "West Midlands",
#     "NHS Durham Dales, Easington and Sedgefield CCG": "North East England",
#     "NHS Ealing CCG": "London",
#     "NHS East and North Hertfordshire CCG": "East of England",
#     "NHS East Lancashire CCG": "North West England",
#     "NHS East Leicestershire and Rutland CCG": "East Midlands",
#     "NHS East Riding of Yorkshire CCG": "Yorkshire and the Humber",
#     "NHS East Staffordshire CCG": "West Midlands",
#     "NHS East Surrey CCG": "South East England",
#     "NHS Eastbourne, Hailsham and Seaford CCG": "South East England",
#     "NHS Eastern Cheshire CCG": "North West England",
#     "NHS Enfield CCG": "London",
#     "NHS Erewash CCG": "East Midlands",
#     "NHS Fareham and Gosport CCG": "South East England",
#     "NHS Fylde & Wyre CCG": "North West England",
#     "NHS Gloucestershire CCG": "South West England",
#     "NHS Great Yarmouth and Waveney CCG": "East of England",
#     "NHS Greater Huddersfield CCG": "Yorkshire and the Humber",
#     "NHS Greater Preston CCG": "North West England",
#     "NHS Greenwich CCG": "London",
#     "NHS Guildford and Waverley CCG": "South East England",
#     "NHS Halton CCG": "North West England",
#     "NHS Hambleton, Richmondshire and Whitby CCG": "Yorkshire and the Humber",
#     "NHS Hammersmith and Fulham CCG": "London",
#     "NHS Hardwick CCG": "East Midlands",
#     "NHS Haringey CCG": "London",
#     "NHS Harrogate and Rural District CCG": "Yorkshire and the Humber",
#     "NHS Harrow CCG": "London",
#     "NHS Hartlepool and Stockton-On-Tees CCG": "North East England",
#     "NHS Hastings and Rother CCG": "South East England",
#     "NHS Havering CCG": "London",
#     "NHS Herefordshire CCG": "West Midlands",
#     "NHS Herts Valleys CCG": "East of England",
#     "NHS Heywood, Middleton and Rochdale CCG": "North West England",
#     "NHS High Weald Lewes Havens CCG": "South East England",
#     "NHS Hillingdon CCG": "London",
#     "NHS Horsham and Mid Sussex CCG": "South East England",
#     "NHS Hounslow CCG": "London",
#     "NHS Hull CCG": "Yorkshire and the Humber",
#     "NHS Ipswich and East Suffolk CCG": "East of England",
#     "NHS Isle of Wight CCG": "South East England",
#     "NHS Islington CCG": "London",
#     "NHS Kernow CCG": "South West England",
#     "NHS Kingston CCG": "London",
#     "NHS Knowsley CCG": "North West England",
#     "NHS Lambeth CCG": "London",
#     "NHS Lancashire North CCG": "North West England",
#     "NHS Leeds North CCG": "Yorkshire and the Humber",
#     "NHS Leeds South and East CCG": "Yorkshire and the Humber",
#     "NHS Leeds West CCG": "Yorkshire and the Humber",
#     "NHS Leicester City CCG": "East Midlands",
#     "NHS Lewisham CCG": "London",
#     "NHS Lincolnshire East CCG": "East Midlands",
#     "NHS Lincolnshire West CCG": "East Midlands",
#     "NHS Liverpool CCG": "North West England",
#     "NHS Luton CCG": "East of England",
#     "NHS Mansfield and Ashfield CCG": "East Midlands",
#     "NHS Medway CCG": "South East England",
#     "NHS Merton CCG": "London",
#     "NHS Mid Essex CCG": "East of England",
#     "NHS Milton Keynes CCG": "South East England",
#     "NHS Nene CCG": "East of England",
#     "NHS Newark & Sherwood CCG": "East Midlands",
#     "NHS Newbury and District CCG": "South East England",
#     "NHS Newcastle Gateshead CCG": "North East England",
#     "NHS Newham CCG": "London",
#     "NHS North & West Reading CCG": "South East England",
#     "NHS North Derbyshire CCG": "East Midlands",
#     "NHS North Durham CCG": "North East England",
#     "NHS North East Essex CCG": "East of England",
#     "NHS North East Hampshire and Farnham CCG": "South East England",
#     "NHS North East Lincolnshire CCG": "Yorkshire and the Humber",
#     "NHS North Hampshire CCG": "South East England",
#     "NHS North Kirklees CCG": "Yorkshire and the Humber",
#     "NHS North Lincolnshire CCG": "Yorkshire and the Humber",
#     "NHS North Manchester CCG": "North West England",
#     "NHS North Norfolk CCG": "East of England",
#     "NHS North Somerset CCG": "South West England",
#     "NHS North Staffordshire CCG": "West Midlands",
#     "NHS North Tyneside CCG": "North East England",
#     "NHS North West Surrey CCG": "South East England",
#     "NHS North, East, West Devon CCG": "South West England",
#     "NHS Northumberland CCG": "North East England",
#     "NHS Norwich CCG": "East of England",
#     "NHS Nottingham City CCG": "East Midlands",
#     "NHS Nottingham North and East CCG": "East Midlands",
#     "NHS Nottingham West CCG": "East Midlands",
#     "NHS Oldham CCG": "North West England",
#     "NHS Oxfordshire CCG": "South East England",
#     "NHS Portsmouth CCG": "South East England",
#     "NHS Redbridge CCG": "London",
#     "NHS Redditch and Bromsgrove CCG": "West Midlands",
#     "NHS Richmond CCG": "London",
#     "NHS Rotherham CCG": "Yorkshire and the Humber",
#     "NHS Rushcliffe CCG": "East Midlands",
#     "NHS Salford CCG": "North West England",
#     "NHS Sandwell and West Birmingham CCG": "West Midlands",
#     "NHS Scarborough and Ryedale CCG": "Yorkshire and the Humber",
#     "NHS Sheffield CCG": "Yorkshire and the Humber",
#     "NHS Shropshire CCG": "West Midlands",
#     "NHS Slough CCG": "South East England",
#     "NHS Solihull CCG": "West Midlands",
#     "NHS Somerset CCG": "South West England",
#     "NHS South Cheshire CCG": "North West England",
#     "NHS South Devon and Torbay CCG": "South West England",
#     "NHS South East Staffs and Seisdon Peninsular CCG": "West Midlands",
#     "NHS South Eastern Hampshire CCG": "South East England",
#     "NHS South Gloucestershire CCG": "South West England",
#     "NHS South Kent Coast CCG": "South East England",
#     "NHS South Lincolnshire CCG": "East Midlands",
#     "NHS South Manchester CCG": "North West England",
#     "NHS South Norfolk CCG": "East of England",
#     "NHS South Reading CCG": "South East England",
#     "NHS South Sefton CCG": "North West England",
#     "NHS South Tees CCG": "North East England",
#     "NHS South Tyneside CCG": "North East England",
#     "NHS South Warwickshire CCG": "West Midlands",
#     "NHS South West Lincolnshire CCG": "East Midlands",
#     "NHS South Worcestershire CCG": "West Midlands",
#     "NHS Southampton CCG": "South East England",
#     "NHS Southend CCG": "East of England",
#     "NHS Southern Derbyshire CCG": "East Midlands",
#     "NHS Southport and Formby CCG": "North West England",
#     "NHS Southwark CCG": "London",
#     "NHS St Helens CCG": "North West England",
#     "NHS Stafford and Surrounds CCG": "West Midlands",
#     "NHS Stockport CCG": "North West England",
#     "NHS Stoke on Trent CCG": "West Midlands",
#     "NHS Sunderland CCG": "North East England",
#     "NHS Surrey Downs CCG": "South East England",
#     "NHS Surrey Heath CCG": "South East England",
#     "NHS Sutton CCG": "London",
#     "NHS Swale CCG": "South East England",
#     "NHS Swindon CCG": "South West England",
#     "NHS Tameside and Glossop CCG": "North West England",
#     "NHS Telford and Wrekin CCG": "West Midlands",
#     "NHS Thanet CCG": "South East England",
#     "NHS Thurrock CCG": "East of England",
#     "NHS Tower Hamlets CCG": "London",
#     "NHS Trafford CCG": "North West England",
#     "NHS Vale of York CCG": "Yorkshire and the Humber",
#     "NHS Vale Royal CCG": "North West England",
#     "NHS Wakefield CCG": "Yorkshire and the Humber",
#     "NHS Walsall CCG": "West Midlands",
#     "NHS Waltham Forest CCG": "London",
#     "NHS Wandsworth CCG": "London",
#     "NHS Warrington CCG": "North West England",
#     "NHS Warwickshire North CCG": "West Midlands",
#     "NHS West Cheshire CCG": "North West England",
#     "NHS West Essex CCG": "East of England",
#     "NHS West Hampshire CCG": "South East England",
#     "NHS West Kent CCG": "South East England",
#     "NHS West Lancashire CCG": "North West England",
#     "NHS West Leicestershire CCG": "East Midlands",
#     "NHS West London (K&C & QPP) CCG": "London",
#     "NHS West Norfolk CCG": "East of England",
#     "NHS West Suffolk CCG": "East of England",
#     "NHS Wigan Borough CCG": "North West England",
#     "NHS Wiltshire CCG": "South West England",
#     "NHS Windsor, Ascot and Maidenhead CCG": "South East England",
#     "NHS Wirral CCG": "North West England",
#     "NHS Wokingham CCG": "South East England",
#     "NHS Wolverhampton CCG": "West Midlands",
#     "NHS Wyre Forest CCG": "West Midlands",
#     "NHS Birmingham Crosscity CCG":	"West Midlands"

# }

# # Assuming you have a DataFrame containing the CCG data (replace 'ccg_data' with your DataFrame)
# ccgdata['Region'] = ccgdata['Area'].apply(lambda area: region_mapping.get(area, "Not Found"))

# # Print the DataFrame with the new 'Region' column
# # Save the updated DataFrame to a new CSV file (optional)
# ccgdata.to_csv('data_with_regions.csv', index=False)

#  
final_data=get_data()
st.sidebar.header("Filter By:")
year = st.sidebar.multiselect("Year", final_data["Year"].unique())
if year:
    final_data1= final_data[final_data["Year"].isin(year)]
else:
    final_data1 = final_data.copy()

region = st.sidebar.multiselect("Region",final_data["Region"].unique())
#Create region filter
if region:
    df1= final_data1[final_data1["Region"].isin(region)]
else:
    df1 = final_data1.copy()
#Create area filter
area = st.sidebar.multiselect("CCG",df1["Area"].unique())
if area:
    filtered_df= df1[df1["Area"].isin(area)]
else:
    filtered_df = df1.copy()
# # Overall Summary
st.title("Health Data Insights")
met1,met2,met3,met4 = st.columns(4)
with met1:
    st.metric("Total Individuals", filtered_df['Number'].agg('sum'))
with met2:
    st.metric("Diabetes Prevalence", round(filtered_df['Prevalence'].agg('mean'), 2), "%")


# Top region with diabetes
top_region = (
    filtered_df.groupby("Region")["Prevalence"]
    .agg('mean')
    #.transpose()
    .reset_index()
    .sort_values(by="Prevalence", ascending=False).head(1)

)
#Top 5 areas with diabetes
top_area_diabetes = (
    filtered_df.groupby('Area')['Prevalence']
    .mean()
    .reset_index()
    .sort_values('Prevalence', ascending=False).iloc[0]
)


with met3:
    #st.subheader("Rgion with the highest Diabetes Prevalence")
    for index, row in top_region.iterrows():
        st.metric(f"Top Region", row['Region'])
        st.metric(f"Prevalence", round(row['Prevalence'], 2), "%")

with met4:
    
    st.metric(f" Top CCG", top_area_diabetes['Area'])
    st.metric(f"Prevalence", round( top_area_diabetes['Prevalence'], 2), "%")




if region:
    # Group data by Year and prevalence
    diabetes_prevalence = (
        filtered_df.groupby(["Year","Area"])["Prevalence"]
        .agg('mean')
        .round(4)
        .reset_index()
    )

    prevalence_data = diabetes_prevalence
    # Create the line chart using Plotly
    fig = px.line(
        prevalence_data, x="Year", y="Prevalence", title="Diabetes Prevalence by Year",
        hover_data=["Area","Year", "Prevalence"],color="Area"
        
    )
    fig.update_layout(xaxis_title="Year", yaxis_title="Prevalence (%)") 

    # Display the chart using Streamlit
    st.title("Diabetes Prevalence by Year")
    st.plotly_chart(fig)
else:
        # Group data by Year and prevalence
    diabetes_prevalence = (
        filtered_df.groupby(["Year","Region"])["Prevalence"]
        .agg('mean')
        .round(4)
        .reset_index()
    )

    prevalence_data = diabetes_prevalence
    # Create the line chart using Plotly
    fig = px.line(
        prevalence_data, x="Year", y="Prevalence", title="Diabetes Prevalence by Year",
        hover_data=["Region","Year", "Prevalence"],color="Region"
        
    )
    fig.update_layout(xaxis_title="Year", yaxis_title="Prevalence (%)") 

    # Display the chart using Streamlit
    st.title("Diabetes Prevalence by Year")
    st.plotly_chart(fig)


m,n = st.columns(2)
# Heatmap visualizing prevalence rates across different regions
if region:
    fig = px.bar(
    filtered_df,
    x="Year",
    y="Prevalence",
    color="Area",
    barmode="group",
    title="Prevalence by CCG  and Year")
    with m:
        st.plotly_chart(fig)

    fig = px.imshow(filtered_df.pivot_table(index='Area', columns='Year', values='Prevalence'),
                    title="Diabetes Prevalence by CCG and Year")
                    #title = (f"Top Region"{reg}))
    fig.update_layout(xaxis_title="Year", yaxis_title="CCG")
    with n:
        st.plotly_chart(fig)

    
else:
    fig = px.bar(
    filtered_df.groupby(['Region','Year'])['Prevalence'].agg('mean').reset_index(),
    x="Year",
    y="Prevalence",
    color="Region",
    barmode="group",
    title="Prevalence by Region  and Year")
    with m:
        st.plotly_chart(fig)

    fig = px.imshow(filtered_df.pivot_table(index='Region', columns='Year', values='Prevalence'),
                    title="Diabetes Prevalence by Region and Year")
    fig.update_layout(xaxis_title="Year", yaxis_title="Region")
    with n:
        st.plotly_chart(fig)
    




# Load the shapefile containing region boundaries
#@st.cache_data
def get_merged():
    shapefile_path = 'Clinical_Commissioning_Groups_July_2015_FEB_in_England.shp'
    regions_gdf_shp = gpd.read_file(shapefile_path)
    regions_gdf= pd.read_csv("CCG.csv",encoding="ISO-8859-1")
    regions_gdf1= pd.read_csv("CCG2.csv",encoding="ISO-8859-1")

        # Merge data and shapefile based on a common column (e.g., region name)
    merged_data1 = pd.merge(filtered_df, regions_gdf, on=['Area_code','Area'], how='left')
    merged_data = pd.merge(merged_data1, regions_gdf1, on=['Area_code','Area'], how='left')

    df_dropped = merged_data.drop([ 'ï»¿OBJECTID_x','Shape_Area_x','Shape_Length_x','GlobalID_x','ï»¿OBJECTID_y'], axis=1)

    df_dropped = df_dropped[df_dropped['LAT'].notna()]

    df_dropped=df_dropped.rename(columns={"LONG": "LON","Shape_Length_y":"Shape_Length","Shape_Area_y":"Shape_Area","GlobalID_y":"GlobalID"}, errors="raise")

    regions_gdf_shp=regions_gdf_shp.rename(columns={"ccg15cd":"Area_code","ccg15nm": "Area"})
    #st.write(merged_data.isnull().dropna)
    df_dropped= pd.merge(df_dropped,regions_gdf_shp, on =['Area_code','Area','GlobalID'], how='left')
    #st.write(df_dropped.head(5))
    #df_dropped.to_csv('merged_data_shp.csv', index=False)
    #st.write(df_dropped.columns)
    #st.map(df_dropped)
    return df_dropped
df_dropped = get_merged()
gdf = gpd.GeoDataFrame(df_dropped, geometry=df_dropped.geometry)

gdf = gdf.reset_index(drop=True).set_index('Area')

# Display the map using Streamlit
#st.plotly_chart(m)

if gdf.geometry.geom_type[0] == 'Point':
    gdf['geometry'] = gdf.buffer(0)  # Create polygons with zero radius
# Create a GeoDataFrame
gdf = gpd.GeoDataFrame(df_dropped, geometry=df_dropped.geometry)
fig = px.scatter_mapbox(
    gdf,
    lat="LAT",
    lon="LON",
    color="Area",  # Adjust color based on Shape_Area
    size="Prevalence",  # Adjust size based on Shape_Length
    mapbox_style="open-street-map",
    zoom=5  # Adjust zoom level as needed
)


st.plotly_chart(fig)

# import sys
# sys.setrecursionlimit(15000)  # Increase the recursion limit to 10000
# df_dropped['geometry'] = df_dropped.geometry.to_json()
# df_dropped.columns = df_dropped.columns.astype(str)
# #df_dropped = df_dropped.dropna(subset=['GlobalID_y'])
# df_dropped = df_dropped.reset_index(drop=True).set_index('Area')
# fig = px.choropleth(df_dropped, geojson=df_dropped.geometry, locations=df_dropped.index, color='Area_code', color_continuous_scale="Viridis", projection="mercator")
# fig.update_geos(fitbounds="locations", visible=True)
# st.plotly_chart(fig)

# # Create a GeoDataFrame
# gdf = gpd.GeoDataFrame(df_dropped, geometry=df_dropped.geometry)
# gdf.crs = 'EPSG:4326'  # Set the CRS to WGS84
# # # Convert points to polygons if necessary
# if gdf.geometry.geom_type[0] == 'Point':
#     gdf['geometry'] = gdf.buffer(0)  # Create polygons with zero radius


# fig = px.choropleth_mapbox(
#     gdf,
#     geojson=gdf['geometry'],
#     locations=gdf.index,
#     color="Number",  # Replace with your column name
#     mapbox_style="open-street-map",
#     zoom=5  # Adjust zoom level as needed
# )
# st.plotly_chart(fig)
# #fig.show()
