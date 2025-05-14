# ==========================================================
# marker.py
import re as regex  # Have to do this because re conflicts with sympy

# ==========================================================
async def mark_example(inSans, inCans) -> str:
  print(3, inSans, inCans)
  sans = await decode_sans(inSans)
  cans = await decode_cans(inCans)
  print(6, sans, cans)
  if cans[0] == 2:
    return await mark_example2(sans[0], cans[1])

  return 'ok'
# ==========================================================
async def decode_sans(inSans) -> list:
  lst = []
  if 'sans=' in inSans:
    tmp = inSans.replace('sans=', '')
    return [tmp]
  return lst
# ==========================================================
async def decode_cans(inCans) -> list:
  lst = []
  if 'cans=' in inCans:
    tmp = inCans.replace('cans=', '')
    tmp1 = tmp.split(':')
    tmp1[0] = int(tmp1[0])
    return tmp1
  return lst
# ==========================================================
# Identical strings
async def mark_example2(inSans, inCans) -> str:
  print(29, inSans, inCans)
  sans = regex.sub(r'\s+', '', inSans)  # remove whitespace
  cans = regex.sub(r'\s+', '', inCans)  # remove whitespace
  if sans == cans: return 'ok'
  return 'bad'
# ==========================================================
