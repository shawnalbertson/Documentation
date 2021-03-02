###
# Renaming columns
###

# All to lower case
df_lower = df.rename(str.lower, axis = 'columns')
# Select columns
df_aircraft.rename(
    # Provide a dict to define new names for columns
    {
        # original_name : new_name
        "Citation 500 Series": "citation",
        "MDAT 30": "mdat30",
        "MDAT 50": "mdat50",
    }, 
    axis=1 # axis = 1 denotes columns (rather than rows)
)

###
# Load CSV
###
df_aircraft = pd.read_csv(filename_aircraft)