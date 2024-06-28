from auth_util import AuthUtilSession
from chat_util import ChatUtilSession

# email = "test_1@navatechgroup.com"
auth_conn = AuthUtilSession(auth_server_url="https://authentication-nai-eu1-aws.dev.infra.navatechgroup.com/",
                            auth_realm_name="chat",
                            auth_client_id="nAI",
                            auth_secret_key="Ao5C2AlHonvRRfEaq2B2fcdiWKOmcO7u",
                            auth_user_secret_key="q2B2fcdiWKOmc"
                            )

# user_id = auth_conn.create_auth_user(username=email, email=email)
# #
info = auth_conn.get_auth_token("paras.anadani@navatechgroup.com")
# info = auth_conn.decode_auth_token("eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJuYTBLSUwyVWZfUkluZ1c4NWFzczZTc1NLOEZaVWFWWEs5NWlac0lNSG1ZIn0.eyJleHAiOjE3MDg2NzA3OTEsImlhdCI6MTcwODU4NDM5MSwianRpIjoiNmU2NzQ3ZWUtMGJmZC00YWI0LTkyYTktOTM2ZmIzMDFmNzQxIiwiaXNzIjoiaHR0cHM6Ly9hdXRoZW50aWNhdGlvbi1uYWktZGV2LWV1MS1hd3Muc3RhZ2UuaW5mcmEubmF2YXRlY2hncm91cC5jb20vcmVhbG1zL2NoYXQiLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiMzIzMThlZWMtNTQ3ZC00YzE4LThlMTUtZDljZTQxNDNjMDI0IiwidHlwIjoiQmVhcmVyIiwiYXpwIjoibkFJIiwic2Vzc2lvbl9zdGF0ZSI6IjQ5NjIxYzViLTFkMmMtNDI1Yi05MGIyLTA2ODk4MTFjZDNiOCIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiLyoiXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImRlZmF1bHQtcm9sZXMtY2hhdCIsIm9mZmxpbmVfYWNjZXNzIiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwic2lkIjoiNDk2MjFjNWItMWQyYy00MjViLTkwYjItMDY4OTgxMWNkM2I4IiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInByZWZlcnJlZF91c2VybmFtZSI6ImVlNzk2YThhLWZkN2ItNDU2NS1iZDVkLTk4YzI4OGZhZjNkY0BtYWlsaW5hdG9yLmNvbSIsImVtYWlsIjoiZWU3OTZhOGEtZmQ3Yi00NTY1LWJkNWQtOThjMjg4ZmFmM2RjQG1haWxpbmF0b3IuY29tIn0.ZDM_yz-RDw1saQCZ_SnWqSmeRDrESkADHVldyg0JZQtEhFhdEqU0VRVsbIPq2Hri35kRwu9t16XJyhY-XDzh-eIIUkwe9xZVtkUnNs4Ygq_vtwgEy-G10p_SbatosLfPA4qvyd8TWl8kA6Kee2Xwb4ecLU--KSvsefOO9wq6zqN2Iwfthu47REyeGZGwZ3PVCCNKDAX9Anue5k2oYzopq5JFqMJ8ERHUEsoSSuiwFq1noVLeZw58k9BVmawQUumKOPMTkNq9k-2kWOaRrGJj-cvUp1pmMg_XGIhBwq15JDZ_e0CPALVsb1VR4MFObP0roQX3Swfi26qKEZK5TSv6IQ")
print(info)

# auth_conn = AuthUtilSession(auth_server_url="http://0.0.0.0:3011/",
#                             auth_realm_name="chat",
#                             auth_client_id="neom",
#                             auth_secret_key="McyPlprzOhhbclwU60P46hVwYm3lfthD",
#                             auth_user_secret_key="uadmin"
#                             )
#
# # user_id = auth_conn.create_auth_user(username=email, email=email)
# #
# info = auth_conn.get_auth_token("965f5ed1-f455-4266-99a6-7f10d1fb7927@msbctest.com")
# print(info)
# chat_conn = ChatUtilSession(
#     chat_admin_id = "yzAoNtF6r27ByceJD",
#         chat_admin_token = "1x2nhwCAAieKshQ9vV96VrT2H-85xBk2bsEhjdMc5C9",
#         chat_server_url = "http://0.0.0.0:3002",
#         chat_user_secret_key = "6JCjUUdjirSaEjiIZhdyqQ",
#         chat_email_domain = "neom.com",
#         chat_admin_user = "navatech",
#         chat_admin_password = "admin")
#
# response = chat_conn.delete_chat_user("2db2fb0c-a8bd-4a55-bd35-4ccc965c2e69")
# print(response)
## invalid token
# user = auth_conn.decode_auth_token("eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJYLTQ0eUVUOWhnamxBWG40YjlBd2JDX0xXSUNwTEJqSnVucDUwV21FRTU0In0.eyJleHAiOjE2ODkzMTcxMDksImlhdCI6MTY4OTMxNjgwOSwianRpIjoiODhhNjA4ZGYtMWUxNC00OGU5LWEyYWUtZTkzMDY0NjhmOGFjIiwiaXNzIjoiaHR0cDovLzAuMC4wLjA6MzAwMS9yZWFsbXMvY2hhdCIsImF1ZCI6ImFjY291bnQiLCJzdWIiOiJhMDAzNTNiMS1iODYxLTQxMjAtYWY5Ny1lYzcwYzhjMTRmMTQiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJuZW9tIiwic2Vzc2lvbl9zdGF0ZSI6ImEzMTZlMzViLTlkY2QtNGQ5Ny1hZDNmLWEzMDMwZGU4Yzk4MyIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiLyoiXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImRlZmF1bHQtcm9sZXMtcm9ja2V0X2NoYXQiLCJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJvcGVuaWQgZW1haWwgcHJvZmlsZSIsInNpZCI6ImEzMTZlMzViLTlkY2QtNGQ5Ny1hZDNmLWEzMDMwZGU4Yzk4MyIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJ0ZXN0XzFAbmF2YXRlY2hncm91cC5jb20iLCJlbWFpbCI6InRlc3RfMUBuYXZhdGVjaGdyb3VwLmNvbSJ9.KQd0AEC0SqonCj0Tuew4awiQHEbm_tw9VLR5gccCepxABo8jgOKlN8mnBza9ne38lSiADcsSkUs5Bx0GWjpNIXNwARtP6dQfcgJXbKqUo_tNPNHDPwIi2dYePYDBPm2mQIHxB7i2H6S8kFAL79BfsbJz9lT9_cJCEEUlygXyLxuOaGJ_qWIATKD5op5eLLu38kJ5fZNAGGB7oGHiNUL2_rNFZrd2ZGvfurDqW0l7uqChJYsHLw4oQWK-j2E7VDn9qOuVghfXHjJs2cbuVPEJBzRfoFtumvYcwsIVclu1FV_2SaYBaiP2pi8QbelUfLDau9qhQsxAp2Gx44clb2E7eg")
# print(user)

## valid token
# user = auth_conn.decode_auth_token("eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJYLTQ0eUVUOWhnamxBWG40YjlBd2JDX0xXSUNwTEJqSnVucDUwV21FRTU0In0.eyJleHAiOjE2ODk2NjE2NjcsImlhdCI6MTY4OTY2MTM2NywianRpIjoiNDA2NWQwYTMtYjJhMS00YmU1LWIyZTktMzQ2OWRiNDgyM2MzIiwiaXNzIjoiaHR0cDovLzAuMC4wLjA6MzAwMS9yZWFsbXMvY2hhdCIsImF1ZCI6ImFjY291bnQiLCJzdWIiOiJlZmI4M2FmMy0yMWEyLTRlM2QtODQ5Yi05ZTkxZTdlMzA4MGQiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJuZW9tIiwic2Vzc2lvbl9zdGF0ZSI6ImEyMzg0MDk2LTU1MWMtNDU0NC04M2M5LTU4NzE2MmVlYTU5ZSIsImFjciI6IjEiLCJhbGxvd2VkLW9yaWdpbnMiOlsiLyoiXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImRlZmF1bHQtcm9sZXMtcm9ja2V0X2NoYXQiLCJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJvcGVuaWQgZW1haWwgcHJvZmlsZSIsInNpZCI6ImEyMzg0MDk2LTU1MWMtNDU0NC04M2M5LTU4NzE2MmVlYTU5ZSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJlZWVhMDVjYS04NWZhLTQ4MzctYmYzOS05MjhhMzc4MmJlMWUiLCJnaXZlbl9uYW1lIjoiIiwiZmFtaWx5X25hbWUiOiIiLCJlbWFpbCI6Imt1bWFyQHNpZGVwb2NrZXQuY29tIn0.LX-77u-69TVA02WeUB4li8MtosFbyy4elQYjTMy-OfvakSTL3UL29HFnEm-qjpuhq3MA8k1HY2VSmW8h15gv79AbTopmq8kLRRp5U-v-uDRvghrbZ-CceVKNm78b8ROVHBj5_FKMD35a0VXSvX-VvBxFsDNYDTxX-uHE5XT2kp72jyKZ-KT3IdQ3-AmkGDRif81Op6HEjQSUhCTZMtSkBZKKG2CbIApUUSH8xkNU3ov9eU-07ZWHutofFbu42up_vCTAvBOM_omJHchNtNCr8-HRk91rbT8KBieiUHqitPZaXYCFJ8m-dDMByJ1983RShtR_iq-P2uWSmrZYoCSVvA")
# print(user)
