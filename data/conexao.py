from supabase import create_client, Client

url: str = "https://bowzlifqrgnpypeaffhc.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJvd3psaWZxcmducHlwZWFmZmhjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTU3Nzk1MzIsImV4cCI6MjA3MTM1NTUzMn0.Mt8MztlDpbeMuRBPLDcyCSuzdclI8MKqP8ZjK_4cq-s"
supabase: Client = create_client(url, key) # Realiza a conexão com o Supabase

