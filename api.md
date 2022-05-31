vendorIdentifier:"TOWER_ADA"

itemCategoryHashes:[] 2 items
0:59 // <ItemCategory "Mods">
1:4104513227 // <ItemCategory "Armor Mods">

itemType:19 // enum DestinyItemType "Mod"

Ada-1 > categories > 8 [List of all available combat mods]

Mods 128-223

+ categories are indices for the rows in the vendor menus ingame -> second row, 3rd and 4th index are current vendor combat style
mods!!!!

+ Vendors/350061650/?components=401 (VendorCategories)
+ -> categories > data > categories > 1 > 2 && 3 

+ Destiny2.GetVendor/Vendor:35001650 
+ -> > itemlist

+ Destiny2.GetCollectibleNodeDetails?characterId=&destinyMembershipId=&membershipType=&components=800&collectiblePresentationNodeHash=123185593 (123185593 == combat style mods)
+ -> collectibles > data > collectibles > itemhash > state (64 for aquired mods, 65 for not aquired)
