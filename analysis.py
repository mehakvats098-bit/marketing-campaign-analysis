import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("data/marketing_campaign.csv")

# Create marketing metrics
data["CTR"] = (data["Clicks"] / data["Impressions"]) * 100

data["Conversion_Rate"] = (
    data["Conversions"] / data["Clicks"]
) * 100

data["ROAS"] = data["Revenue"] / data["Spend"]

# Round metrics
data["CTR"] = data["CTR"].round(2)
data["Conversion_Rate"] = data["Conversion_Rate"].round(2)
data["ROAS"] = data["ROAS"].round(2)

# -----------------------------------
# Channel-level analysis
# -----------------------------------

channel_analysis = data.groupby("Channel").agg(
    Total_Impressions=("Impressions", "sum"),
    Total_Clicks=("Clicks", "sum"),
    Total_Conversions=("Conversions", "sum"),
    Total_Spend=("Spend", "sum"),
    Total_Revenue=("Revenue", "sum")
).reset_index()

# Calculate channel-level metrics
channel_analysis["CTR"] = (
    channel_analysis["Total_Clicks"]
    / channel_analysis["Total_Impressions"]
) * 100

channel_analysis["Conversion_Rate"] = (
    channel_analysis["Total_Conversions"]
    / channel_analysis["Total_Clicks"]
) * 100

channel_analysis["ROAS"] = (
    channel_analysis["Total_Revenue"]
    / channel_analysis["Total_Spend"]
)

# Round results
channel_analysis["CTR"] = channel_analysis["CTR"].round(2)
channel_analysis["Conversion_Rate"] = channel_analysis["Conversion_Rate"].round(2)
channel_analysis["ROAS"] = channel_analysis["ROAS"].round(2)

# Display results
print("\nChannel Performance:")
print(channel_analysis)

# Save results
channel_analysis.to_csv(
    "channel_performance.csv",
    index=False
)

print("\nChannel analysis saved successfully!")
# -----------------------------------
# ROAS by channel
# -----------------------------------

plt.figure(figsize=(8, 5))

plt.bar(
    channel_analysis["Channel"],
    channel_analysis["ROAS"]
)

plt.title("ROAS by Marketing Channel")
plt.xlabel("Marketing Channel")
plt.ylabel("ROAS")

plt.tight_layout()

plt.savefig("charts/roas_by_channel.png")

plt.show()
# -----------------------------------
# Conversion Rate by Channel
# -----------------------------------

plt.figure(figsize=(8, 5))

plt.bar(
    channel_analysis["Channel"],
    channel_analysis["Conversion_Rate"]
)

plt.title("Conversion Rate by Marketing Channel")
plt.xlabel("Marketing Channel")
plt.ylabel("Conversion Rate (%)")

plt.tight_layout()

plt.savefig("charts/conversion_rate_by_channel.png")

plt.show()
# -----------------------------------
# Campaign Type Performance
# -----------------------------------

campaign_type_analysis = data.groupby("Campaign_Type").agg(
    Total_Impressions=("Impressions", "sum"),
    Total_Clicks=("Clicks", "sum"),
    Total_Conversions=("Conversions", "sum"),
    Total_Spend=("Spend", "sum"),
    Total_Revenue=("Revenue", "sum")
).reset_index()

campaign_type_analysis["CTR"] = (
    campaign_type_analysis["Total_Clicks"]
    / campaign_type_analysis["Total_Impressions"]
) * 100

campaign_type_analysis["Conversion_Rate"] = (
    campaign_type_analysis["Total_Conversions"]
    / campaign_type_analysis["Total_Clicks"]
) * 100

campaign_type_analysis["ROAS"] = (
    campaign_type_analysis["Total_Revenue"]
    / campaign_type_analysis["Total_Spend"]
)

campaign_type_analysis["CTR"] = campaign_type_analysis["CTR"].round(2)
campaign_type_analysis["Conversion_Rate"] = campaign_type_analysis["Conversion_Rate"].round(2)
campaign_type_analysis["ROAS"] = campaign_type_analysis["ROAS"].round(2)

print("\nCampaign Type Performance:")
print(campaign_type_analysis)

campaign_type_analysis.to_csv(
    "campaign_type_performance.csv",
    index=False
)

print("\nCampaign type analysis saved successfully!")

# -----------------------------------
# Target Audience Performance
# -----------------------------------

audience_analysis = data.groupby("Target_Audience").agg(
    Total_Impressions=("Impressions", "sum"),
    Total_Clicks=("Clicks", "sum"),
    Total_Conversions=("Conversions", "sum"),
    Total_Spend=("Spend", "sum"),
    Total_Revenue=("Revenue", "sum")
).reset_index()

audience_analysis["CTR"] = (
    audience_analysis["Total_Clicks"]
    / audience_analysis["Total_Impressions"]
) * 100

audience_analysis["Conversion_Rate"] = (
    audience_analysis["Total_Conversions"]
    / audience_analysis["Total_Clicks"]
) * 100

audience_analysis["ROAS"] = (
    audience_analysis["Total_Revenue"]
    / audience_analysis["Total_Spend"]
)

audience_analysis["CTR"] = audience_analysis["CTR"].round(2)
audience_analysis["Conversion_Rate"] = audience_analysis["Conversion_Rate"].round(2)
audience_analysis["ROAS"] = audience_analysis["ROAS"].round(2)

print("\nTarget Audience Performance:")
print(audience_analysis)

audience_analysis.to_csv(
    "target_audience_performance.csv",
    index=False
)

print("\nTarget audience analysis saved successfully!")
# -----------------------------------
# Revenue vs Spend
# -----------------------------------

plt.figure(figsize=(8, 5))

plt.scatter(
    data["Spend"],
    data["Revenue"]
)

plt.title("Revenue vs Marketing Spend")
plt.xlabel("Marketing Spend")
plt.ylabel("Revenue")

plt.tight_layout()

plt.savefig("charts/revenue_vs_spend.png")

plt.show()
# -----------------------------------
# Correlation Analysis
# -----------------------------------

correlation_columns = [
    "Impressions",
    "Clicks",
    "Conversions",
    "Spend",
    "Revenue"
]

correlation_matrix = data[correlation_columns].corr()

print("\nCorrelation Matrix:")
print(correlation_matrix.round(2))

correlation_matrix.to_csv(
    "correlation_matrix.csv"
)

print("\nCorrelation analysis saved successfully!")

# -----------------------------------
# Cost Per Conversion
# -----------------------------------

data["Cost_Per_Conversion"] = (
    data["Spend"] / data["Conversions"]
)

data["Cost_Per_Conversion"] = (
    data["Cost_Per_Conversion"].round(2)
)

print("\nCost Per Conversion:")
print(
    data[
        [
            "Campaign_ID",
            "Channel",
            "Campaign_Type",
            "Conversions",
            "Spend",
            "Cost_Per_Conversion"
        ]
    ]
)

data.to_csv(
    "marketing_campaign_analysis.csv",
    index=False
)

print("\nCost per conversion calculated successfully!")

# -----------------------------------
# Cost Per Conversion by Channel
# -----------------------------------

channel_analysis["Cost_Per_Conversion"] = (
    channel_analysis["Total_Spend"]
    / channel_analysis["Total_Conversions"]
)

channel_analysis["Cost_Per_Conversion"] = (
    channel_analysis["Cost_Per_Conversion"].round(2)
)

print("\nCost Per Conversion by Channel:")
print(
    channel_analysis[
        [
            "Channel",
            "Total_Spend",
            "Total_Conversions",
            "Cost_Per_Conversion"
        ]
    ]
)

plt.figure(figsize=(8, 5))

plt.bar(
    channel_analysis["Channel"],
    channel_analysis["Cost_Per_Conversion"]
)

plt.title("Cost Per Conversion by Marketing Channel")
plt.xlabel("Marketing Channel")
plt.ylabel("Cost Per Conversion")

plt.tight_layout()

plt.savefig("charts/cost_per_conversion_by_channel.png")

plt.show()

print("\nCost per conversion chart saved successfully!")
# -----------------------------------
# Final Business Summary
# -----------------------------------

print("\n" + "=" * 50)
print("FINAL BUSINESS SUMMARY")
print("=" * 50)

# Best channel by revenue
best_revenue_channel = channel_analysis.loc[
    channel_analysis["Total_Revenue"].idxmax()
]

print("\nHighest Revenue Channel:")
print(
    f"{best_revenue_channel['Channel']} "
    f"-> ₹{best_revenue_channel['Total_Revenue']:,}"
)

# Best channel by ROAS
best_roas_channel = channel_analysis.loc[
    channel_analysis["ROAS"].idxmax()
]

print("\nHighest ROAS Channel:")
print(
    f"{best_roas_channel['Channel']} "
    f"-> {best_roas_channel['ROAS']}"
)

# Best channel by conversion rate
best_conversion_channel = channel_analysis.loc[
    channel_analysis["Conversion_Rate"].idxmax()
]

print("\nHighest Conversion Rate Channel:")
print(
    f"{best_conversion_channel['Channel']} "
    f"-> {best_conversion_channel['Conversion_Rate']}%"
)

# Best campaign type by revenue
best_campaign_type = campaign_type_analysis.loc[
    campaign_type_analysis["Total_Revenue"].idxmax()
]

print("\nHighest Revenue Campaign Type:")
print(
    f"{best_campaign_type['Campaign_Type']} "
    f"-> ₹{best_campaign_type['Total_Revenue']:,}"
)

# Best audience by ROAS
best_audience = audience_analysis.loc[
    audience_analysis["ROAS"].idxmax()
]

print("\nHighest ROAS Target Audience:")
print(
    f"{best_audience['Target_Audience']} "
    f"-> {best_audience['ROAS']}"
)

print("\n" + "=" * 50)
print("Analysis completed successfully!")
print("=" * 50)