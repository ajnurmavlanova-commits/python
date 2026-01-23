import pandas as pd
import sqlite3

conn = sqlite3.connect("task\\chinook.db")
customers = pd.read_sql_query("SELECT * FROM customers", conn)
invoices = pd.read_sql_query("SELECT * FROM invoices", conn)
1.customer_spending = invoices.groupby('CustomerId')['Total'].sum().reset_index()
customer_spending.rename(columns={'Total': 'TotalSpent'}, inplace=True)
2.top_5_customers = customer_spending.sort_values(
    by='TotalSpent', ascending=False
).head(5)
3.top_5_details = top_5_customers.merge(
    customers,
    on='CustomerId'
)[['CustomerId', 'FirstName', 'LastName', 'TotalSpent']]

print("Top 5 Customers by Total Purchase Amount:")
print(top_5_details)

invoice_items = pd.read_sql_query("SELECT * FROM invoice_items", conn)
tracks = pd.read_sql_query("SELECT * FROM tracks", conn)
albums = pd.read_sql_query("SELECT * FROM albums", conn)

merged = invoice_items.merge(tracks, on='TrackId')
merged = merged.merge(invoices[['InvoiceId', 'CustomerId']], on='InvoiceId')

album_track_counts = tracks.groupby('AlbumId')['TrackId'].count().reset_index()
album_track_counts.rename(columns={'TrackId': 'TotalAlbumTracks'}, inplace=True)

customer_album_purchases = (
    merged.groupby(['CustomerId', 'AlbumId'])['TrackId']
    .count()
    .reset_index(name='TracksBought')
)

customer_album_purchases = customer_album_purchases.merge(
    album_track_counts,
    on='AlbumId'
)

customer_album_purchases['PurchaseType'] = customer_album_purchases.apply(
    lambda x: 'Full Album' if x['TracksBought'] == x['TotalAlbumTracks']
    else 'Individual Tracks',
    axis=1
)

customer_preference = (
    customer_album_purchases.groupby('CustomerId')['PurchaseType']
    .apply(lambda x: 'Individual Tracks' if 'Individual Tracks' in x.values else 'Full Album')
)

preference_counts = customer_preference.value_counts(normalize=True) * 100

summary = preference_counts.reset_index()
summary.columns = ['PurchasePreference', 'Percentage']

print("\nCustomer Purchase Preference Summary (%):")
print(summary)

conn.close()

