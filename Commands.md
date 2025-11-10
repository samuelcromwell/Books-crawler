(venv) ➜  Books-crawler git:(main) export API_KEY="efea65f1177cdf9c2760d8836ea3696ccdfb4a86162fd6c9ea7501e0844874c1"
(venv) ➜  Books-crawler git:(main) curl -s -H "X-API-Key: $API_KEY" "http://localhost:9010/books?page=1&page_size=10" \
  | python -m json.tool

{
    "page": 1,
    "page_size": 10,
    "pages": 41,
    "total": 402,
    "items": [
        {
            "id": "69119bf92d95a6c0fb518484",
            "product_url": "https://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html",
            "upc": "a22124811bfa8350",
            "name": "It's Only the Himalayas",
            "description": "\u201cWherever you go, whatever you do, just . . . don\u2019t do anything stupid.\u201d \u2014My MotherDuring her yearlong adventure backpacking from South Africa to Singapore, S. Bedford definitely did a few things her mother might classify as \"stupid.\" She swam with great white sharks in South Africa, ran from lions in Zimbabwe, climbed a Himalayan mountain without training in Nepal, and wa \u201cWherever you go, whatever you do, just . . . don\u2019t do anything stupid.\u201d \u2014My MotherDuring her yearlong adventure backpacking from South Africa to Singapore, S. Bedford definitely did a few things her mother might classify as \"stupid.\" She swam with great white sharks in South Africa, ran from lions in Zimbabwe, climbed a Himalayan mountain without training in Nepal, and watched as her friend was attacked by a monkey in Indonesia.But interspersed in those slightly more crazy moments, Sue Bedfored and her friend \"Sara the Stoic\" experienced the sights, sounds, life, and culture of fifteen countries. Joined along the way by a few friends and their aging fathers here and there, Sue and Sara experience the trip of a lifetime. They fall in love with the world, cultivate an appreciation for home, and discover who, or what, they want to become.It's Only the Himalayas is the incredibly funny, sometimes outlandish, always entertaining confession of a young backpacker that will inspire you to take your own adventure. ...more",
            "category": "Travel",
            "price_incl_tax": 45.17,
            "price_excl_tax": 45.17,
            "availability": 19,
            "num_reviews": 0,
            "image_url": "https://books.toscrape.com/media/cache/6d/41/6d418a73cc7d4ecfd75ca11d854041db.jpg",
            "rating": 2,
            "content_hash": "1b629cc81963b0046d76dd1e3eff4714a64afb7e73f038c36c4170ca93a6b8e8",
            "updated_at": "2025-11-10T08:02:01.054000",
            "crawl_meta": {
                "ts": "2025-11-10T08:02:01.054000",
                "status": "ok",
                "source_url": "https://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html"
            },
            "created_at": "2025-11-10T08:02:01.054000"
        },
        {
            "id": "69119bf92d95a6c0fb518486",
            "product_url": "https://books.toscrape.com/catalogue/full-moon-over-noahs-ark-an-odyssey-to-mount-ararat-and-beyond_811/index.html",
            "upc": "ce60436f52c5ee68",
            "name": "Full Moon over Noah\u2019s Ark: An Odyssey to Mount Ararat and Beyond",
            "description": "Acclaimed travel writer Rick Antonson sets his adventurous compass on Mount Ararat, exploring the region\u2019s long history, religious mysteries, and complex politics.Mount Ararat is the most fabled mountain in the world. For millennia this massif in eastern Turkey has been rumored as the resting place of Noah\u2019s Ark following the Great Flood. But it also plays a significant ro Acclaimed travel writer Rick Antonson sets his adventurous compass on Mount Ararat, exploring the region\u2019s long history, religious mysteries, and complex politics.Mount Ararat is the most fabled mountain in the world. For millennia this massif in eastern Turkey has been rumored as the resting place of Noah\u2019s Ark following the Great Flood. But it also plays a significant role in the longstanding conflict between Turkey and Armenia.Author Rick Antonson joined a five-member expedition to the mountain\u2019s nearly 17,000-foot summit, trekking alongside a contingent of Armenians, for whom Mount Ararat is the stolen symbol of their country. Antonson weaves vivid historical anecdote with unexpected travel vignettes, whether tracing earlier mountaineering attempts on the peak, recounting the genocide of Armenians and its unresolved debate, or depicting the Kurds\u2019 ambitions for their own nation\u2019s borders, which some say should include Mount Ararat.What unfolds in Full Moon Over Noah\u2019s Ark is one man\u2019s odyssey, a tale told through many stories. Starting with the flooding of the Black Sea in 5600 BCE, through to the Epic of Gilgamesh and the contrasting narratives of the Great Flood known to followers of the Judaic, Christian and Islamic religions, Full Moon Over Noah\u2019s Ark takes readers along with Antonson through the shadows and broad landscapes of Turkey, Iraq, Iran and Armenia, shedding light on a troubled but fascinating area of the world. ...more",
            "category": "Travel",
            "price_incl_tax": 49.43,
            "price_excl_tax": 49.43,
            "availability": 15,
            "num_reviews": 0,
            "image_url": "https://books.toscrape.com/media/cache/fe/8a/fe8af6ceec7718986380c0fde9b3b34f.jpg",
            "rating": 4,
            "content_hash": "89a3c9cd67d4a8958b37c761cec7b415664e4e49299d77a06155b81fed79b6f3",
            "updated_at": "2025-11-10T08:02:01.326000",
            "crawl_meta": {
                "ts": "2025-11-10T08:02:01.326000",
                "status": "ok",
                "source_url": "https://books.toscrape.com/catalogue/full-moon-over-noahs-ark-an-odyssey-to-mount-ararat-and-beyond_811/index.html"
            },
            "created_at": "2025-11-10T08:02:01.326000"
        },
        {
            "id": "69119bf92d95a6c0fb518488",
            "product_url": "https://books.toscrape.com/catalogue/see-america-a-celebration-of-our-national-parks-treasured-sites_732/index.html",
            "upc": "f9705c362f070608",
            "name": "See America: A Celebration of Our National Parks & Treasured Sites",
            "description": "To coincide with the 2016 centennial anniversary of the National Parks Service, the Creative Action Network has partnered with the National Parks Conservation Association to revive and reimagine the legacy of WPA travel posters. Artists from all over the world have participated in the creation of this new, crowdsourced collection of See America posters for a modern era. Fe To coincide with the 2016 centennial anniversary of the National Parks Service, the Creative Action Network has partnered with the National Parks Conservation Association to revive and reimagine the legacy of WPA travel posters. Artists from all over the world have participated in the creation of this new, crowdsourced collection of See America posters for a modern era. Featuring artwork for 75 national parks and monuments across all 50 states, this engaging keepsake volume celebrates the full range of our nation's landmarks and treasured wilderness. ...more",
            "category": "Travel",
            "price_incl_tax": 48.87,
            "price_excl_tax": 48.87,
            "availability": 14,
            "num_reviews": 0,
            "image_url": "https://books.toscrape.com/media/cache/c7/1a/c71a85dbf8c2dbc75cb271026618477c.jpg",
            "rating": 3,
            "content_hash": "335f29ce60d8be582c55fae284acf77693e2ab231dd165f29c4fde503e85dbe1",
            "updated_at": "2025-11-10T08:02:01.595000",
            "crawl_meta": {
                "ts": "2025-11-10T08:02:01.595000",
                "status": "ok",
                "source_url": "https://books.toscrape.com/catalogue/see-america-a-celebration-of-our-national-parks-treasured-sites_732/index.html"
            },
            "created_at": "2025-11-10T08:02:01.595000"
        },
        {
            "id": "69119bf92d95a6c0fb51848a",
            "product_url": "https://books.toscrape.com/catalogue/vagabonding-an-uncommon-guide-to-the-art-of-long-term-world-travel_552/index.html",
            "upc": "1809259a5a5f1d8d",
            "name": "Vagabonding: An Uncommon Guide to the Art of Long-Term World Travel",
            "description": "With a new foreword by Tim Ferriss \u2022There\u2019s nothing like vagabonding: taking time off from your normal life\u2014from six weeks to four months to two years\u2014to discover and experience the world on your own terms. In this one-of-a-kind handbook, veteran travel writer Rolf Potts explains how anyone armed with an independent spirit can achieve the dream of extended overseas travel. With a new foreword by Tim Ferriss \u2022\u00a0There\u2019s nothing like vagabonding: taking time off from your normal life\u2014from six weeks to four months to two years\u2014to discover and experience the world on your own terms. In this one-of-a-kind handbook, veteran travel writer Rolf Potts explains how anyone armed with an independent spirit can achieve the dream of extended overseas travel. Now completely revised and updated, Vagabonding is an accessible and inspiring guide to \u00a0 \u2022 financing your travel time \u2022 determining your destination \u2022 adjusting to life on the road \u2022 working and volunteering overseas \u2022\u00a0handling travel adversity \u2022 re-assimilating back into ordinary life \u00a0Praise for Vagabonding\u00a0 \u201cA crucial reference for any budget wanderer.\u201d\u2014Time\u00a0 \u201cVagabonding easily remains in my top-10 list of life-changing books. Why? Because one incredible trip, especially a long-term trip, can change your life forever. And Vagabonding teaches you how to travel (and think), not just for one trip, but for the rest of your life.\u201d\u2014Tim Ferriss, from the foreword \u00a0 \u201cThe book is a meditation on the joys of hitting the road. . . . It\u2019s also a primer for those with a case of pent-up wanderlust seeking to live the dream.\u201d\u2014USA Today \u00a0 \u201cI couldn\u2019t put this book down. It\u2019s a whole different ethic of travel. . . . [Potts\u2019s] practical advice might just convince you to enjoy that open-ended trip of a lifetime.\u201d\u2014Rick Steves \u00a0 \u201cPotts wants us to wander, to explore, to embrace the unknown, and, finally, to take our own damn time about it. I think this is the most sensible book of travel-related advice ever written.\u201d\u2014Tim Cahill, founding editor of Outside ...more",
            "category": "Travel",
            "price_incl_tax": 36.94,
            "price_excl_tax": 36.94,
            "availability": 8,
            "num_reviews": 0,
            "image_url": "https://books.toscrape.com/media/cache/ca/30/ca30b1afe1e76ce7ba1db8176d398e53.jpg",
            "rating": 2,
            "content_hash": "cc6177cd058d133b5f941a22c5f6dc339ffac9d5b557ef2cbb41fa4852099974",
            "updated_at": "2025-11-10T08:02:01.868000",
            "crawl_meta": {
                "ts": "2025-11-10T08:02:01.868000",
                "status": "ok",
                "source_url": "https://books.toscrape.com/catalogue/vagabonding-an-uncommon-guide-to-the-art-of-long-term-world-travel_552/index.html"
            },
            "created_at": "2025-11-10T08:02:01.868000"
        },
        {
            "id": "69119bfa2d95a6c0fb51848c",
            "product_url": "https://books.toscrape.com/catalogue/under-the-tuscan-sun_504/index.html",
            "upc": "a94350ee74deaa07",
            "name": "Under the Tuscan Sun",
            "description": "A CLASSIC FROM THE BESTSELLING AUTHOR OF UNDER MAGNOLIAFrances Mayes\u2014widely published poet, gourmet cook, and travel writer\u2014opens the door to a wondrous new world when she buys and restores an abandoned villa in the spectacular Tuscan countryside. In evocative language, she brings the reader along as she discovers the beauty and simplicity of life in Italy. Mayes also crea A CLASSIC FROM THE BESTSELLING AUTHOR OF UNDER MAGNOLIAFrances Mayes\u2014widely published poet, gourmet cook, and travel writer\u2014opens the door to a wondrous new world when she buys and restores an abandoned villa in the spectacular Tuscan countryside. In evocative language, she brings the reader along as she discovers the beauty and simplicity of life in Italy. Mayes also creates dozens of delicious seasonal recipes from her traditional kitchen and simple garden, all of which she includes in the book. Doing for Tuscany what M.F.K. Fisher and Peter Mayle did for Provence, Mayes writes about the tastes and pleasures of a foreign country with gusto and passion. ...more",
            "category": "Travel",
            "price_incl_tax": 37.33,
            "price_excl_tax": 37.33,
            "availability": 7,
            "num_reviews": 0,
            "image_url": "https://books.toscrape.com/media/cache/45/21/4521c581ba727f5c835e34860cbf53e5.jpg",
            "rating": 3,
            "content_hash": "f1ef235959565e971f40fdc4b6e9543c9c5cc5faab424f130645d3d3e74308d7",
            "updated_at": "2025-11-10T08:02:02.133000",
            "crawl_meta": {
                "ts": "2025-11-10T08:02:02.133000",
                "status": "ok",
                "source_url": "https://books.toscrape.com/catalogue/under-the-tuscan-sun_504/index.html"
            },
            "created_at": "2025-11-10T08:02:02.133000"
        },
        {
            "id": "69119bfa2d95a6c0fb51848e",
            "product_url": "https://books.toscrape.com/catalogue/a-summer-in-europe_458/index.html",
            "upc": "cc1936a9f4e93477",
            "name": "A Summer In Europe",
            "description": "On her thirtieth birthday, Gwendolyn Reese receives an unexpected present from her widowed Aunt Bea: a grand tour of Europe in the company of Bea's Sudoku and Mahjongg Club. The prospect isn't entirely appealing. But when the gift she is expecting--an engagement ring from her boyfriend--doesn't materialize, Gwen decides to go. At first, Gwen approaches the trip as if it's On her thirtieth birthday, Gwendolyn Reese receives an unexpected present from her widowed Aunt Bea: a grand tour of Europe in the company of Bea's Sudoku and Mahjongg Club. The prospect isn't entirely appealing. But when the gift she is expecting--an engagement ring from her boyfriend--doesn't materialize, Gwen decides to go. At first, Gwen approaches the trip as if it's the math homework she assigns her students, diligently checking monuments off her must-see list. But amid the bougainvillea and stunning vistas of southern Italy, something changes. Gwen begins to live in the moment--skipping down stone staircases in Capri, running her fingers over a glacier in view of the Matterhorn, racing through the Louvre, and taste-testing pastries at a Marseilles cafe. Reveling in every new experience--especially her attraction to a charismatic British physics professor--Gwen discovers that the ancient wonders around her are nothing compared to the renaissance unfolding within. . . \"A thinking woman's love story, it swept me away to breathtaking places with a cast of endearing characters I won't soon forget. Bravissima!\" Susan McBride, author of \"Little Black Dress\" Praise for Marilyn Brant's According to Jane \"A warm, witty and charmingly original story.\" --Susan Wiggs, \"New York Times \" bestselling author \"Brant infuses her sweetly romantic and delightfully clever tale with just the right dash of Austen-esque wit.\" \"Chicago Tribune\" \"An engaging read for all who have been through the long, dark, dating wars, and still believe there's sunshine, and a Mr. Darcy, at the end of the tunnel.\" --Cathy Lamb, author of \"Such a Pretty Face\"\" ...more",
            "category": "Travel",
            "price_incl_tax": 44.34,
            "price_excl_tax": 44.34,
            "availability": 7,
            "num_reviews": 0,
            "image_url": "https://books.toscrape.com/media/cache/6c/e3/6ce3003931701c7a3fd5354917538ea9.jpg",
            "rating": 2,
            "content_hash": "86db872a894b162d0b924cd9a27a59cff91b8f45ae91ff4a8aa182b63c692104",
            "updated_at": "2025-11-10T08:02:02.416000",
            "crawl_meta": {
                "ts": "2025-11-10T08:02:02.416000",
                "status": "ok",
                "source_url": "https://books.toscrape.com/catalogue/a-summer-in-europe_458/index.html"
            },
            "created_at": "2025-11-10T08:02:02.416000"
        },
        {
            "id": "69119bfa2d95a6c0fb518490",
            "product_url": "https://books.toscrape.com/catalogue/the-great-railway-bazaar_446/index.html",
            "upc": "48736df57e7bec9f",
            "name": "The Great Railway Bazaar",
            "description": "First published more than thirty years ago, Paul Theroux's strange, unique, and hugely entertaining railway odyssey has become a modern classic of travel literature. Here Theroux recounts his early adventures on an unusual grand continental tour. Asia's fabled trains -- the Orient Express, the Khyber Pass Local, the Frontier Mail, the Golden Arrow to Kuala Lumpur, the Mand First published more than thirty years ago, Paul Theroux's strange, unique, and hugely entertaining railway odyssey has become a modern classic of travel literature. Here Theroux recounts his early adventures on an unusual grand continental tour. Asia's fabled trains -- the Orient Express, the Khyber Pass Local, the Frontier Mail, the Golden Arrow to Kuala Lumpur, the Mandalay Express, the Trans-Siberian Express -- are the stars of a journey that takes him on a loop eastbound from London's Victoria Station to Tokyo Central, then back from Japan on the Trans-Siberian. Brimming with Theroux's signature humor and wry observations, this engrossing chronicle is essential reading for both the ardent adventurer and the armchair traveler. ...more",
            "category": "Travel",
            "price_incl_tax": 30.54,
            "price_excl_tax": 30.54,
            "availability": 6,
            "num_reviews": 0,
            "image_url": "https://books.toscrape.com/media/cache/d5/82/d582f6b0261c2842330e893962276295.jpg",
            "rating": 1,
            "content_hash": "9329649ae3d8b46fe987f272cbd7618754b0da0ae68046d80943a52dd045fc3e",
            "updated_at": "2025-11-10T08:02:02.696000",
            "crawl_meta": {
                "ts": "2025-11-10T08:02:02.696000",
                "status": "ok",
                "source_url": "https://books.toscrape.com/catalogue/the-great-railway-bazaar_446/index.html"
            },
            "created_at": "2025-11-10T08:02:02.696000"
        },
        {
            "id": "69119bfa2d95a6c0fb518492",
            "product_url": "https://books.toscrape.com/catalogue/a-year-in-provence-provence-1_421/index.html",
            "upc": "9e60929f521fa280",
            "name": "A Year in Provence (Provence #1)",
            "description": "National BestsellerIn this witty and warm-hearted account, Peter Mayle tells what it is like to realize a long-cherished dream and actually move into a 200-year-old stone farmhouse in the remote country of the Lub\u00e9ron with his wife and two large dogs. He endures January's frosty mistral as it comes howling down the Rh\u00f4ne Valley, discovers the secrets of goat racing through National Bestseller\u00a0In this witty and warm-hearted account, Peter Mayle tells what it is like to realize a long-cherished dream and actually move into a 200-year-old stone farmhouse in the remote country of the Lub\u00e9ron with his wife and two large dogs. He endures January's frosty mistral as it comes howling down the Rh\u00f4ne Valley, discovers the secrets of goat racing through the middle of town, and delights in the glorious regional cuisine. A Year in Provence transports us into all the earthy pleasures of Proven\u00e7al life and lets us live vicariously at a tempo governed by seasons, not by days. ...more",
            "category": "Travel",
            "price_incl_tax": 56.88,
            "price_excl_tax": 56.88,
            "availability": 6,
            "num_reviews": 0,
            "image_url": "https://books.toscrape.com/media/cache/8b/81/8b81cd9b2c8f89a12099a80bed1c4911.jpg",
            "rating": 4,
            "content_hash": "2bccfc08c887f9b1489f225c889b03608bc673fedb1000abd4a03ab842c89665",
            "updated_at": "2025-11-10T08:02:02.978000",
            "crawl_meta": {
                "ts": "2025-11-10T08:02:02.978000",
                "status": "ok",
                "source_url": "https://books.toscrape.com/catalogue/a-year-in-provence-provence-1_421/index.html"
            },
            "created_at": "2025-11-10T08:02:02.978000"
        },
        {
            "id": "69119bfb2d95a6c0fb518494",
            "product_url": "https://books.toscrape.com/catalogue/the-road-to-little-dribbling-adventures-of-an-american-in-britain-notes-from-a-small-island-2_277/index.html",
            "upc": "366a236aa1ea6f07",
            "name": "The Road to Little Dribbling: Adventures of an American in Britain (Notes From a Small Island #2)",
            "description": "The hilarious and loving sequel to a hilarious and loving classic of travel writing: Notes from a Small Island, Bill Bryson\u2019s valentine to his adopted country of EnglandIn 1995 Bill Bryson got into his car and took a weeks-long farewell motoring trip about England before moving his family back to the United States. The book about that trip, Notes from a Small Island, is up The hilarious and loving sequel to a hilarious and loving classic of travel writing: Notes from a Small Island, Bill Bryson\u2019s valentine to his adopted country of EnglandIn 1995 Bill Bryson got into his car and took a weeks-long farewell motoring trip about England before moving his family back to the United States. The book about that trip, Notes from a Small Island, is uproarious and endlessly endearing, one of the most acute and affectionate portrayals of England in all its glorious eccentricity ever written. Two decades later, he set out again to rediscover that country, and the result is The Road to Little Dribbling. Nothing is funnier than Bill Bryson on the road\u2014prepare for the total joy and multiple episodes of unseemly laughter. ...more",
            "category": "Travel",
            "price_incl_tax": 23.21,
            "price_excl_tax": 23.21,
            "availability": 3,
            "num_reviews": 0,
            "image_url": "https://books.toscrape.com/media/cache/26/f5/26f5d20239a45046e756c6d09611b3ea.jpg",
            "rating": 1,
            "content_hash": "d3e192916e14e8cc38395d8a687d861987b699e04b796e6f3f0a69709a13a106",
            "updated_at": "2025-11-10T08:02:03.253000",
            "crawl_meta": {
                "ts": "2025-11-10T08:02:03.253000",
                "status": "ok",
                "source_url": "https://books.toscrape.com/catalogue/the-road-to-little-dribbling-adventures-of-an-american-in-britain-notes-from-a-small-island-2_277/index.html"
            },
            "created_at": "2025-11-10T08:02:03.253000"
        },
        {
            "id": "69119bfb2d95a6c0fb518496",
            "product_url": "https://books.toscrape.com/catalogue/neither-here-nor-there-travels-in-europe_198/index.html",
            "upc": "747cf7fca2ccdbd4",
            "name": "Neither Here nor There: Travels in Europe",
            "description": "Bill Bryson's first travel book, The Lost Continent, was unanimously acclaimed as one of the funniest books in years. In Neither Here nor There he brings his unique brand of humour to bear on Europe as he shoulders his backpack, keeps a tight hold on his wallet, and journeys from Hammerfest, the northernmost town on the continent, to Istanbul on the cusp of Asia. Fluent in Bill Bryson's first travel book, The Lost Continent, was unanimously acclaimed as one of the funniest books in years. In Neither Here nor There he brings his unique brand of humour to bear on Europe as he shoulders his backpack, keeps a tight hold on his wallet, and journeys from Hammerfest, the northernmost town on the continent, to Istanbul on the cusp of Asia. Fluent in, oh, at least one language, he retraces his travels as a student twenty years before.Whether braving the homicidal motorist of Paris, being robbed by gypsies in Florence, attempting not to order tripe and eyeballs in a German restaurant, window-shopping in the sex shops of the Reeperbahn or disputing his hotel bill in Copenhagen, Bryson takes in the sights, dissects the culture and illuminates each place and person with his hilariously caustic observations. He even goes to Liechtenstein. ...more",
            "category": "Travel",
            "price_incl_tax": 38.95,
            "price_excl_tax": 38.95,
            "availability": 3,
            "num_reviews": 0,
            "image_url": "https://books.toscrape.com/media/cache/c9/9a/c99a7a05537cd842eb4db83d537e3a4d.jpg",
            "rating": 3,
            "content_hash": "05b98b0fcca11acb6cbc5aa623d0bd9ad8b75e1dc14b3653ed33150b953e9bbc",
            "updated_at": "2025-11-10T08:02:03.523000",
            "crawl_meta": {
                "ts": "2025-11-10T08:02:03.523000",
                "status": "ok",
                "source_url": "https://books.toscrape.com/catalogue/neither-here-nor-there-travels-in-europe_198/index.html"
            },
            "created_at": "2025-11-10T08:02:03.523000"
        }
    ]
}
(venv) ➜  Books-crawler git:(main) curl -s -H "X-API-Key: $API_KEY" \
  "http://localhost:9010/books?category=Mystery&min_price=10&max_price=30&sort_by=price&page=1&page_size=10" \
  | python -m json.tool

{
    "page": 1,
    "page_size": 10,
    "pages": 2,
    "total": 19,
    "items": [
        {
            "id": "69119bfe2d95a6c0fb5184a8",
            "product_url": "https://books.toscrape.com/catalogue/tastes-like-fear-di-marnie-rome-3_742/index.html",
            "upc": "2d1e337aaf341858",
            "name": "Tastes Like Fear (DI Marnie Rome #3)",
            "description": "Sarah Hilary won the 2015 Theakston's Crime Novel of the Year with her debut, the 2014 Richard and Judy pick SOMEONE ELSE'S SKIN. She followed up with NO OTHER DARKNESS, proclaimed as 'riveting' by Lisa Gardner and 'truly mesmerising' by David Mark. Now D.I. Marnie Rome returns in her third novel.Home is where Harm lies...The young girl who causes the fatal car crash disap Sarah Hilary won the 2015 Theakston's Crime Novel of the Year with her debut, the 2014 Richard and Judy pick SOMEONE ELSE'S SKIN. She followed up with NO OTHER DARKNESS, proclaimed as 'riveting' by Lisa Gardner and 'truly mesmerising' by David Mark. Now D.I. Marnie Rome returns in her third novel.Home is where Harm lies...The young girl who causes the fatal car crash disappears from the scene.A runaway who doesn't want to be found, she only wants to go home.To the one man who understands her.Gives her shelter. Just as he gives shelter to the other lost girls who live in his house.He's the head of her new family.He's Harm. And when Harm's family is threatened, Marnie Rome is about to find out that everything tastes like fear... ...more",
            "category": "Mystery",
            "price_incl_tax": 10.69,
            "price_excl_tax": 10.69,
            "availability": 14,
            "num_reviews": 0,
            "image_url": "https://books.toscrape.com/media/cache/74/9b/749bca168778cf35fdb2441a9d6b403f.jpg",
            "rating": 1,
            "content_hash": "587cf9d441651f294c11ca0cfcc25e5b37ea2c5519e5aed4c14bc7aa130b6fdd",
            "updated_at": "2025-11-10T08:02:06.246000",
            "crawl_meta": {
                "ts": "2025-11-10T08:02:06.246000",
                "status": "ok",
                "source_url": "https://books.toscrape.com/catalogue/tastes-like-fear-di-marnie-rome-3_742/index.html"
            },
            "created_at": "2025-11-10T08:02:06.246000"
        },
        {
            "id": "69119bff2d95a6c0fb5184b4",
            "product_url": "https://books.toscrape.com/catalogue/hide-away-eve-duncan-20_620/index.html",
            "upc": "bddc6fd036eb6279",
            "name": "Hide Away (Eve Duncan #20)",
            "description": "Iris Johansen's beloved forensic sculptor Eve Duncan is back and now the stakes are higher than ever. Dramatic changes are on the horizon for Eve and Joe Quinn and their relationship may never be the same. Faced with the task of protecting Cara Delaney, a young girl with ruthless enemies who want to see her dead, Eve takes her away to the remote Scottish Highlands where th Iris Johansen's beloved forensic sculptor Eve Duncan is back and now the stakes are higher than ever. Dramatic changes are on the horizon for Eve and Joe Quinn and their relationship may never be the same. Faced with the task of protecting Cara Delaney, a young girl with ruthless enemies who want to see her dead, Eve takes her away to the remote Scottish Highlands where they join Jane MacGuire in search of a hidden treasure. But nowhere is far enough away to protect Cara from danger. With enemies closing in from all sides, Hide Away is a high-octane thriller that fans will not want to miss. ...more",
            "category": "Mystery",
            "price_incl_tax": 11.84,
            "price_excl_tax": 11.84,
            "availability": 12,
            "num_reviews": 0,
            "image_url": "https://books.toscrape.com/media/cache/b2/c5/b2c501b848bccd9cc375771f53c0fb6e.jpg",
            "rating": 1,
            "content_hash": "5f52b1ae0ebdaa4256de789749a4b2884705f6ed921c34b8f68082aff3725619",
            "updated_at": "2025-11-10T08:02:07.851000",
            "crawl_meta": {
                "ts": "2025-11-10T08:02:07.851000",
                "status": "ok",
                "source_url": "https://books.toscrape.com/catalogue/hide-away-eve-duncan-20_620/index.html"
            },
            "created_at": "2025-11-10T08:02:07.851000"
        },
        {
            "id": "69119c042d95a6c0fb5184d2",
            "product_url": "https://books.toscrape.com/catalogue/the-girl-you-lost_66/index.html",
            "upc": "4280ac3eab57aa5d",
            "name": "The Girl You Lost",
            "description": "Eighteen years ago your baby daughter was snatched. Today, she came back. A sinister and darkly compelling psychological thriller from the No.1 bestselling author of The Girl With No Past. Eighteen years ago, Simone Porter\u2019s six-month-old daughter, Helena, was abducted. Simone and husband, Matt, have slowly rebuilt their shattered lives, but the pain at losing their child Eighteen years ago your baby daughter was snatched. Today, she came back. A sinister and darkly compelling psychological thriller from the No.1 bestselling author of The Girl With No Past. Eighteen years ago, Simone Porter\u2019s six-month-old daughter, Helena, was abducted. Simone and husband, Matt, have slowly rebuilt their shattered lives, but the pain at losing their child has never left them. Then a young woman, Grace, appears out of the blue and tells Simone she has information about her stolen baby. But just who is Grace \u2013 and can Simone trust her? When Grace herself disappears, Simone becomes embroiled in a desperate search for her daughter and the woman who has vital clues about her whereabouts. Simone is inching closer to the truth but it\u2019ll take her into dangerous and disturbing territory. Simone lost her baby. Will she lose her life trying to find her? Read what people are saying about the Number One Bestseller, The Girl With No Past: \u2018I read this in a day and found myself totally engaged with the plot. Kathryn Croft has pulled off a very accessible mystery, that exceeded my expectations and shows her talent. The ending was just right! Worth a read if you fancy a well paced mystery, on these dark autumnal nights.\u2019 Northern Crime \u2018Kept the tension and mystery going right until the end \u2026 An intense read that keeps you turning page after page.\u2019 Crime Book Club \u2018Wow! This book grabbed me from the very beginning! \u2026 To say this book is a page turner would be an understatement!\u2019 Chat About Books \u2018It kept me up all night and cost me my beauty sleep! I will get it out of the way immediately and tell you that this is one of the best thrillers I have read this year and it is fully deserving of my 5-star rating.\u2019 Books Are Man\u2019s Other Best Friend \u2018BLIMEY. This book is GRIPPY - I sat and read it over the course of a day and a night, purely because I couldn't put it down.\u2019 Reading Room with a View \u2018The reader is kept guessing until the end. It's perfection for a thriller and the author does amazingly to keep our intrigue.\u2019 Chic Toronto \u2018Gripping, a real page turner\u2026 Excellent plot, and gripping stuff, that keeps the reader guessing until the end \u2026 raced to the end to find out what was happening and how it would all end \u2026 what a storyteller Kathryn Croft is!\u2019 Emma\u2019s Book Reviews \u2018The concept of this book, and the story itself is phenomenal - honestly one of the best i have read, it really does outshine all other thrillers i have read.\u2019 Afternoon Bookery \u2018I really enjoyed this from start to finish. It's one of these books where you just HAVE to read JUST a couple more pages to see what is going to happen next. The author is very good at building suspense and revealing details bit by bit. It was totally unpredictable and had some very good twists. ...more",
            "category": "Mystery",
            "price_incl_tax": 12.29,
            "price_excl_tax": 12.29,
            "availability": 1,
            "num_reviews": 0,
            "image_url": "https://books.toscrape.com/media/cache/28/15/2815974db428ea019fc84e08af23095b.jpg",
            "rating": 5,
            "content_hash": "75281c7549e7cd18fab8add2275881c538e765c9906ada91774f63fbcdd0df45",
            "updated_at": "2025-11-10T08:02:12.225000",
            "crawl_meta": {
                "ts": "2025-11-10T08:02:12.225000",
                "status": "ok",
                "source_url": "https://books.toscrape.com/catalogue/the-girl-you-lost_66/index.html"
            },
            "created_at": "2025-11-10T08:02:12.225000"
        },
        {
            "id": "69119c002d95a6c0fb5184ba",
            "product_url": "https://books.toscrape.com/catalogue/playing-with-fire_602/index.html",
            "upc": "05a61a3bd8ca4149",
            "name": "Playing with Fire",
            "description": "A beautiful violinist is haunted by a very old piece of music she finds in a strange antique shop in Rome.The first time Julia Ansdell picks up The Incendio Waltz, she knows it\u2019s a strikingly unusual composition. But while playing the piece, Julia blacks out and awakens to find her young daughter implicated in acts of surprising violence. And when she travels to Venice to A beautiful violinist is haunted by a very old piece of music she finds in a strange antique shop in Rome.The first time Julia Ansdell picks up The Incendio Waltz, she knows it\u2019s a strikingly unusual composition. But while playing the piece, Julia blacks out and awakens to find her young daughter implicated in acts of surprising violence. And when she travels to Venice to find the previous owner of the music, she uncovers a dark secret that involves dangerously powerful people\u2014a family who would stop at nothing to keep Julia from bringing the truth to light. ...more",
            "category": "Mystery",
            "price_incl_tax": 13.71,
            "price_excl_tax": 13.71,
            "availability": 11,
            "num_reviews": 0,
            "image_url": "https://books.toscrape.com/media/cache/09/02/0902666ade8ab8183363e53c108e5069.jpg",
            "rating": 3,
            "content_hash": "de6c5bb849b9d0d44fe5e5617d0792f3e4efca62ce5ea1ab3ec9d3468e5a303b",
            "updated_at": "2025-11-10T08:02:08.644000",
            "crawl_meta": {
                "ts": "2025-11-10T08:02:08.644000",
                "status": "ok",
                "source_url": "https://books.toscrape.com/catalogue/playing-with-fire_602/index.html"
            },
            "created_at": "2025-11-10T08:02:08.644000"
        },
        {
            "id": "69119bfd2d95a6c0fb5184a6",
            "product_url": "https://books.toscrape.com/catalogue/that-darkness-gardiner-and-renner-1_743/index.html",
            "upc": "0c7b9cf2b7662b65",
            "name": "That Darkness (Gardiner and Renner #1)",
            "description": "As a forensic investigator for the Cleveland Police Department, Maggie Gardiner has seen her share of Jane Does. The latest is an unidentified female in her early teens, discovered in a local cemetery. More shocking than the girl\u2019s injuries\u2014for Maggie at least\u2014is the fact that no one has reported her missing. She and the detectives assigned to the case (including her cop e As a forensic investigator for the Cleveland Police Department, Maggie Gardiner has seen her share of Jane Does. The latest is an unidentified female in her early teens, discovered in a local cemetery. More shocking than the girl\u2019s injuries\u2014for Maggie at least\u2014is the fact that no one has reported her missing. She and the detectives assigned to the case (including her cop ex-husband) are determined to follow every lead, run down every scrap of evidence. But the monster they seek is watching each move, closer to them than they could ever imagine. Jack Renner is a killer. He doesn\u2019t murder because he savors it, or because he believes himself omnipotent, or for any reason other than to make the world a safer place. When he follows the trail of this Jane Doe to a locked room in a small apartment where eighteen teenaged girls are anything but safe, he knows something must be done. But his pursuit of their captor takes an unexpected turn.Maggie Gardiner finds another body waiting for her in the autopsy room\u2014and a host of questions that will challenge everything she believes about justice, morality, and the true nature of evil \u2026 ...more",
            "category": "Mystery",
            "price_incl_tax": 13.92,
            "price_excl_tax": 13.92,
            "availability": 14,
            "num_reviews": 0,
            "image_url": "https://books.toscrape.com/media/cache/23/b8/23b81994234ac127d701db1531a08e48.jpg",
            "rating": 1,
            "content_hash": "c24c5594fde0cd40e6ca7efa6685f168bc521130058ab43d6462b0b8edb6bbbe",
            "updated_at": "2025-11-10T08:02:05.983000",
            "crawl_meta": {
                "ts": "2025-11-10T08:02:05.983000",
                "status": "ok",
                "source_url": "https://books.toscrape.com/catalogue/that-darkness-gardiner-and-renner-1_743/index.html"
            },
            "created_at": "2025-11-10T08:02:05.983000"
        },
        {
            "id": "69119c042d95a6c0fb5184d4",
            "product_url": "https://books.toscrape.com/catalogue/the-girl-in-the-ice-dci-erika-foster-1_65/index.html",
            "upc": "ee61197edb882599",
            "name": "The Girl In The Ice (DCI Erika Foster #1)",
            "description": "Her eyes are wide open. Her lips parted as if to speak. Her dead body frozen in the ice\u2026She is not the only one. When a young boy discovers the body of a woman beneath a thick sheet of ice in a South London park, Detective Erika Foster is called in to lead the murder investigation. The victim, a beautiful young socialite, appeared to have the perfect life. Yet when Erika b Her eyes are wide open. Her lips parted as if to speak. Her dead body frozen in the ice\u2026She is not the only one. When a young boy discovers the body of a woman beneath a thick sheet of ice in a South London park, Detective Erika Foster is called in to lead the murder investigation. The victim, a beautiful young socialite, appeared to have the perfect life. Yet when Erika begins to dig deeper, she starts to connect the dots between the murder and the killings of three prostitutes, all found strangled, hands bound and dumped in water around London. What dark secrets is the girl in the ice hiding? As Erika inches closer to uncovering the truth, the killer is closing in on Erika. The last investigation Erika led went badly wrong\u2026 resulting in the death of her husband. With her career hanging by a thread, Erika must now battle her own personal demons as well as a killer more deadly than any she\u2019s faced before. But will she get to him before he strikes again?A page-turning thriller packed with suspense. If you like Angela Marsons, Rachel Abbott and Karin Slaughter, discover Rob Bryndza\u2019s new series today \u2013 at a special launch price. Watch out for more from DCI Erika FosterShe\u2019s fearless. Respected. Unstoppable. Detective Erika Foster will catch a killer, whatever it takes. 1. THE GIRL IN THE ICE 2. THE NIGHT STALKER (COMING SOON) ...more",
            "category": "Mystery",
            "price_incl_tax": 15.85,
            "price_excl_tax": 15.85,
            "availability": 1,
            "num_reviews": 0,
            "image_url": "https://books.toscrape.com/media/cache/83/54/835421d17d99c89fd99d07e17806357b.jpg",
            "rating": 3,
            "content_hash": "2ea152a39dc08f4521481c7f60b867fe0ae7ad265be82f9a7e4ef59caeaa2964",
            "updated_at": "2025-11-10T08:02:12.500000",
            "crawl_meta": {
                "ts": "2025-11-10T08:02:12.500000",
                "status": "ok",
                "source_url": "https://books.toscrape.com/catalogue/the-girl-in-the-ice-dci-erika-foster-1_65/index.html"
            },
            "created_at": "2025-11-10T08:02:12.500000"
        },
        {
            "id": "69119bfd2d95a6c0fb5184a0",
            "product_url": "https://books.toscrape.com/catalogue/a-murder-in-time_877/index.html",
            "upc": "f733e8c19d40ec2e",
            "name": "A Murder in Time",
            "description": "Beautiful and brilliant, Kendra Donovan is a rising star at the FBI. Yet her path to professional success hits a speed bump during a disastrous raid where half her team is murdered, a mole in the FBI is uncovered and she herself is severely wounded. As soon as she recovers, she goes rogue and travels to England to assassinate the man responsible for the deaths of her teamm Beautiful and brilliant, Kendra Donovan is a rising star at the FBI. Yet her path to professional success hits a speed bump during a disastrous raid where half her team is murdered, a mole in the FBI is uncovered and she herself is severely wounded. As soon as she recovers, she goes rogue and travels to England to assassinate the man responsible for the deaths of her teammates.While fleeing from an unexpected assassin herself, Kendra escapes into a stairwell that promises sanctuary but when she stumbles out again, she is in the same place - Aldrich Castle - but in a different time: 1815, to be exact.Mistaken for a lady's maid hired to help with weekend guests, Kendra is forced to quickly adapt to the time period until she can figure out how she got there; and, more importantly, how to get back home. However, after the body of a young girl is found on the extensive grounds of the county estate, she starts to feel there's some purpose to her bizarre circumstances. Stripped of her twenty-first century tools, Kendra must use her wits alone in order to unmask a cunning madman. ...more",
            "category": "Mystery",
            "price_incl_tax": 16.64,
            "price_excl_tax": 16.64,
            "availability": 16,
            "num_reviews": 0,
            "image_url": "https://books.toscrape.com/media/cache/cc/bd/ccbd7a62caefd5a3a2e04dd7c2ff48fe.jpg",
            "rating": 1,
            "content_hash": "b084b167573210ed9daccb39b14aafa1379c084e14f1fc457814b6a853c58225",
            "updated_at": "2025-11-10T08:02:05.185000",
            "crawl_meta": {
                "ts": "2025-11-10T08:02:05.185000",
                "status": "ok",
                "source_url": "https://books.toscrape.com/catalogue/a-murder-in-time_877/index.html"
            },
            "created_at": "2025-11-10T08:02:05.185000"
        },
        {
            "id": "69119bfe2d95a6c0fb5184ac",
            "product_url": "https://books.toscrape.com/catalogue/a-study-in-scarlet-sherlock-holmes-1_656/index.html",
            "upc": "63ee5bc46066a8a8",
            "name": "A Study in Scarlet (Sherlock Holmes #1)",
            "description": "In the debut of literature's most famous sleuth, a dead man is discovered in a bloodstained room in Brixton. The only clues are a wedding ring, a gold watch, a pocket edition of Boccaccio's Decameron, and a word scrawled in blood on the wall. With this investigation begins the partnership of Sherlock Holmes and Dr. Watson. Their search for the murderer uncovers a story of In the debut of literature's most famous sleuth, a dead man is discovered in a bloodstained room in Brixton. The only clues are a wedding ring, a gold watch, a pocket edition of Boccaccio's Decameron, and a word scrawled in blood on the wall. With this investigation begins the partnership of Sherlock Holmes and Dr. Watson. Their search for the murderer uncovers a story of love and revenge-and heralds a franchise of detective mysteries starring the formidable Holmes. ...more",
            "category": "Mystery",
            "price_incl_tax": 16.73,
            "price_excl_tax": 16.73,
            "availability": 14,
            "num_reviews": 0,
            "image_url": "https://books.toscrape.com/media/cache/27/40/274003f2720f82844873945b87af6c19.jpg",
            "rating": 2,
            "content_hash": "5760c4388412d94834e9faa537408877ea8332b553dd9590fd9d933e594032c4",
            "updated_at": "2025-11-10T08:02:06.780000",
            "crawl_meta": {
                "ts": "2025-11-10T08:02:06.780000",
                "status": "ok",
                "source_url": "https://books.toscrape.com/catalogue/a-study-in-scarlet-sherlock-holmes-1_656/index.html"
            },
            "created_at": "2025-11-10T08:02:06.780000"
        },
        {
            "id": "69119c032d95a6c0fb5184ca",
            "product_url": "https://books.toscrape.com/catalogue/the-cuckoos-calling-cormoran-strike-1_239/index.html",
            "upc": "1be6d3b121865edb",
            "name": "The Cuckoo's Calling (Cormoran Strike #1)",
            "description": "A BRILLIANT DEBUT MYSTERY IN A CLASSIC VEIN: DETECTIVE CORMORAN STRIKE INVESTIGATES A SUPERMODEL'S SUICIDE. After losing his leg to a land mine in Afghanistan, Cormoran Strike is barely scraping by as a private investigator. Strike is down to one client, and creditors are calling. He has also just broken up with his longtime girlfriend and is living in his office.Then John A BRILLIANT DEBUT MYSTERY IN A CLASSIC VEIN: DETECTIVE CORMORAN STRIKE INVESTIGATES A SUPERMODEL'S SUICIDE. After losing his leg to a land mine in Afghanistan, Cormoran Strike is barely scraping by as a private investigator. Strike is down to one client, and creditors are calling. He has also just broken up with his longtime girlfriend and is living in his office.Then John Bristow walks through his door with an amazing story: His sister, the legendary supermodel Lula Landry, known to her friends as the Cuckoo, famously fell to her death a few months earlier. The police ruled it a suicide, but John refuses to believe that. The case plunges Strike into the world of multimillionaire beauties, rock-star boyfriends, and desperate designers, and it introduces him to every variety of pleasure, enticement, seduction, and delusion known to man.You may think you know detectives, but you've never met one quite like Strike. You may think you know about the wealthy and famous, but you've never seen them under an investigation like this. Introducing Cormoran Strike, this is the acclaimed first crime novel by J.K. Rowling, writing under the pseudonym Robert Galbraith. ...more",
            "category": "Mystery",
            "price_incl_tax": 19.21,
            "price_excl_tax": 19.21,
            "availability": 3,
            "num_reviews": 0,
            "image_url": "https://books.toscrape.com/media/cache/72/ec/72ec24f082aba608ca37bc3aeaf57317.jpg",
            "rating": 1,
            "content_hash": "2afa866eeca27be200d1f1b5940b01f52867bf4b27eea2f4cd0c580f63db343d",
            "updated_at": "2025-11-10T08:02:11.122000",
            "crawl_meta": {
                "ts": "2025-11-10T08:02:11.122000",
                "status": "ok",
                "source_url": "https://books.toscrape.com/catalogue/the-cuckoos-calling-cormoran-strike-1_239/index.html"
            },
            "created_at": "2025-11-10T08:02:11.122000"
        },
        {
            "id": "69119bfc2d95a6c0fb51849c",
            "product_url": "https://books.toscrape.com/catalogue/in-a-dark-dark-wood_963/index.html",
            "upc": "19ed25f4641d5efd",
            "name": "In a Dark, Dark Wood",
            "description": "In a dark, dark wood Nora hasn't seen Clare for ten years. Not since Nora walked out of school one day and never went back. There was a dark, dark houseUntil, out of the blue, an invitation to Clare\u2019s hen do arrives. Is this a chance for Nora to finally put her past behind her?And in the dark, dark house there was a dark, dark roomBut something goes wrong. Very wrong.And i In a dark, dark wood Nora hasn't seen Clare for ten years. Not since Nora walked out of school one day and never went back. There was a dark, dark houseUntil, out of the blue, an invitation to Clare\u2019s hen do arrives. Is this a chance for Nora to finally put her past behind her?And in the dark, dark house there was a dark, dark roomBut something goes wrong. Very wrong.And in the dark, dark room.... Some things can\u2019t stay secret for ever. ...more",
            "category": "Mystery",
            "price_incl_tax": 19.63,
            "price_excl_tax": 19.63,
            "availability": 18,
            "num_reviews": 0,
            "image_url": "https://books.toscrape.com/media/cache/95/84/95840dfd67c020067c99d70451147e20.jpg",
            "rating": 1,
            "content_hash": "08fb446d71abc28ade35b4281a12468830506bf814c10fb3523f1635e2a5b4bf",
            "updated_at": "2025-11-10T08:02:04.628000",
            "crawl_meta": {
                "ts": "2025-11-10T08:02:04.628000",
                "status": "ok",
                "source_url": "https://books.toscrape.com/catalogue/in-a-dark-dark-wood_963/index.html"
            },
            "created_at": "2025-11-10T08:02:04.628000"
        }
    ]
}
(venv) ➜  Books-crawler git:(main) curl -s -H "X-API-Key: $API_KEY" \
  "http://localhost:9010/books?sort_by=rating&page=1&page_size=5" \
  | python -m json.tool

{
    "page": 1,
    "page_size": 5,
    "pages": 81,
    "total": 402,
    "items": [
        {
            "id": "69119cc497046012e128f64d",
            "product_url": "https://books.toscrape.com/catalogue/higherselfie-wake-up-your-life-free-your-soul-find-your-tribe_957/index.html",
            "upc": "c27f6e1f185b0383",
            "name": "#HigherSelfie: Wake Up Your Life. Free Your Soul. Find Your Tribe.",
            "description": "There is a cosmic alarm clock going off around the world! #HigherSelfie's aim is to unite all those waking up spiritually in this digital age. This book is a guide to love, connection, and kickass surrendered action for young people who have at least a toe in the door of spirituality. With a no-nonsense approach and full of wit and humor, this book shares age-old concepts There is a cosmic alarm clock going off around the world! #HigherSelfie's aim is to unite all those waking up spiritually in this digital age. This book is a guide to love, connection, and kickass surrendered action for young people who have at least a toe in the door of spirituality. With a no-nonsense approach and full of wit and humor, this book shares age-old concepts in a language that is accessible to the modern spiritual audience. Whether you have just bought a yoga mat or have been meditating for years, this book will offer you guidance and support, whatever stage of the journey you're at. Life coaches Jo Westwood and Lucy Sheridan touch upon timeless topics such as forgiveness, surrender and the ego, as well as subjects specific to the current age, such as using social media in a healthy way, finding a like-minded tribe, and following your own spiritual and life paths without comparing yourself to others. Whether you're a Reiki master, climbing the corporate ladder or working in a suburban garden center #HigherSelfie will be the perfect \u2018gateway drug\u2019 for those looking for something deeper and more meaningful. ...more",
            "category": "Nonfiction",
            "price_incl_tax": 23.11,
            "price_excl_tax": 23.11,
            "availability": 17,
            "num_reviews": 0,
            "image_url": "https://books.toscrape.com/media/cache/71/45/71451e3bba61a8d888a4a2c6526a4bcf.jpg",
            "rating": 5,
            "content_hash": "ef6d24f89d66e1b8ed3031b08a8bc64edd84b6454137f45454025a0874d0e5d7",
            "updated_at": "2025-11-10T08:05:24.831000",
            "crawl_meta": {
                "ts": "2025-11-10T08:05:24.831000",
                "status": "ok",
                "source_url": "https://books.toscrape.com/catalogue/higherselfie-wake-up-your-life-free-your-soul-find-your-tribe_957/index.html"
            },
            "created_at": "2025-11-10T08:05:24.831000"
        },
        {
            "id": "69119bfb2d95a6c0fb518498",
            "product_url": "https://books.toscrape.com/catalogue/1000-places-to-see-before-you-die_1/index.html",
            "upc": "228ba5e7577e1d49",
            "name": "1,000 Places to See Before You Die",
            "description": "Around the World, continent by continent, here is the best the world has to offer: 1,000 places guaranteed to give travelers the shivers. Sacred ruins, grand hotels, wildlife preserves, hilltop villages, snack shacks, castles, festivals, reefs, restaurants, cathedrals, hidden islands, opera houses, museums, and more. Each entry tells exactly why it's essential to visit. Th Around the World, continent by continent, here is the best the world has to offer: 1,000 places guaranteed to give travelers the shivers. Sacred ruins, grand hotels, wildlife preserves, hilltop villages, snack shacks, castles, festivals, reefs, restaurants, cathedrals, hidden islands, opera houses, museums, and more. Each entry tells exactly why it's essential to visit. Then come the nuts and bolts: addresses, websites, phone and fax numbers, best times to visit. Stop dreaming and get going.This hefty volume reminds vacationers that hot tourist spots are small percentage of what's worth seeing out there. A quick sampling: Venice's Cipriani Hotel; California's Monterey Peninsula; the Lewis and Clark Trail in Oregon; the Great Wall of China; Robert Louis Stevenson's home in Western Samoa; and the Alhambra in Andalusia, Spain. Veteran travel guide writer Schultz divides the book geographically, presenting a little less than a page on each location. Each entry lists exactly where to find the spot (e.g. Moorea is located \"12 miles/19 km northwest of Tahiti; 10 minutes by air, 1 hour by boat\") and when to go (e.g., if you want to check out The Complete Fly Fisher hotel in Montana, \"May and Sept.-Oct. offer productive angling in a solitary setting\"). This is an excellent resource for the intrepid traveler.Copyright 2003 Reed Business Information, Inc. ...more",
            "category": "Travel",
            "price_incl_tax": 26.08,
            "price_excl_tax": 26.08,
            "availability": 1,
            "num_reviews": 0,
            "image_url": "https://books.toscrape.com/media/cache/9e/10/9e106f81f65b293e488718a4f54a6a3f.jpg",
            "rating": 5,
            "content_hash": "8344755d8b5ccc8628d71f281d1fda6d892b760b270d68e60628e8d8a301ca10",
            "updated_at": "2025-11-10T08:02:03.800000",
            "crawl_meta": {
                "ts": "2025-11-10T08:02:03.800000",
                "status": "ok",
                "source_url": "https://books.toscrape.com/catalogue/1000-places-to-see-before-you-die_1/index.html"
            },
            "created_at": "2025-11-10T08:02:03.800000"
        },
        {
            "id": "69119c062d95a6c0fb5184de",
            "product_url": "https://books.toscrape.com/catalogue/a-flight-of-arrows-the-pathfinders-2_876/index.html",
            "upc": "3a6fb983e2554023",
            "name": "A Flight of Arrows (The Pathfinders #2)",
            "description": "October 1776--August 1777It is said that what a man sows he will reap--and for such a harvest there is no set season. No one connected to Reginald Aubrey is untouched by the crime he committed twenty years ago. Not William, the Oneida child Reginald stole and raised as his own. Identity shattered, enlisted in the British army, William trains with Loyalist refugees eager to October 1776--August 1777It is said that what a man sows he will reap--and for such a harvest there is no set season. No one connected to Reginald Aubrey is untouched by the crime he committed twenty years ago. Not William, the Oneida child Reginald stole and raised as his own. Identity shattered, enlisted in the British army, William trains with Loyalist refugees eager to annihilate the rebels who forced them into exile. Coming to terms with who and what he is proves impossible, but if he breaks his Loyalist oath, he'll be no better than the man who constructed his life of lies.Not Anna, Reginald's adopted daughter, nor Two Hawks, William's twin, both who long for Reginald to accept their love despite the challenges they will face, building a marriage that bridges two cultures. Not Good Voice and Stone Thrower, freed of bitterness by a courageous act of forgiveness, but still yearning for their firstborn son and fearful for the future of their Oneida people.As the British prepare to attack frontier New York and Patriot regiments rally to defend it, two families separated by culture, united by love, will do all in their power to reclaim the son marching toward them in the ranks of their enemies. ...more",
            "category": "Historical Fiction",
            "price_incl_tax": 55.53,
            "price_excl_tax": 55.53,
            "availability": 16,
            "num_reviews": 0,
            "image_url": "https://books.toscrape.com/media/cache/ec/65/ec651ed66822d4b68938afa645b1ece2.jpg",
            "rating": 5,
            "content_hash": "aff4a1127d3cbfa7a2a523d9c1deadc8fedf39058530216a0080eac77e6e51ea",
            "updated_at": "2025-11-10T08:02:14.145000",
            "crawl_meta": {
                "ts": "2025-11-10T08:02:14.145000",
                "status": "ok",
                "source_url": "https://books.toscrape.com/catalogue/a-flight-of-arrows-the-pathfinders-2_876/index.html"
            },
            "created_at": "2025-11-10T08:02:14.145000"
        },
        {
            "id": "69119c9f97046012e128f531",
            "product_url": "https://books.toscrape.com/catalogue/a-gentlemans-position-society-of-gentlemen-3_584/index.html",
            "upc": "40c4bf520c17de54",
            "name": "A Gentleman's Position (Society of Gentlemen #3)",
            "description": "Power, privilege, and the rigid rules of class leave two hearts yearning for connection in the sizzling new Society of Gentlemen novel from K. J. Charles. Among his eccentric though strictly principled group of friends, Lord Richard Vane is the confidant on whom everyone depends for advice, moral rectitude, and discreet assistance. Yet when Richard has a problem, he turns Power, privilege, and the rigid rules of class leave two hearts yearning for connection in the sizzling new Society of Gentlemen novel from K. J. Charles.\u00a0 Among his eccentric though strictly principled group of friends, Lord Richard Vane is the confidant on whom everyone depends for advice, moral rectitude, and discreet assistance. Yet when Richard has a problem, he turns to his valet, a fixer of unparalleled genius\u2014and the object of Richard\u2019s deepest desires. If there is one rule a gentleman must follow, it is never to dally with servants. But when David is close enough to touch, the rules of class collide with the basest sort of animal instinct: overpowering lust. \u00a0 For David Cyprian, burglary and blackmail are as much in a day\u2019s work as bootblacking\u2014anything for the man he\u2019s devoted to. But the one thing he wants for himself is the one thing Richard refuses to give: his heart. With the tension between them growing to be unbearable, David\u2019s seemingly incorruptible master has left him no choice. Putting his finely honed skills of seduction and manipulation to good use, he will convince Richard to forget all about his well-meaning objections and give in to sweet, sinful temptation. \u00a0Includes a special message from the editor, as well as an excerpt from another Loveswept title. ...more",
            "category": "Romance",
            "price_incl_tax": 14.75,
            "price_excl_tax": 14.75,
            "availability": 11,
            "num_reviews": 0,
            "image_url": "https://books.toscrape.com/media/cache/82/aa/82aa7770711dfc5edc1f5f69a731d08b.jpg",
            "rating": 5,
            "content_hash": "c6ad124b4d91eeb7ff8323edd93174977d7e97aa4a6e29d2147f8f5b11ec9c95",
            "updated_at": "2025-11-10T08:04:47.565000",
            "crawl_meta": {
                "ts": "2025-11-10T08:04:47.565000",
                "status": "ok",
                "source_url": "https://books.toscrape.com/catalogue/a-gentlemans-position-society-of-gentlemen-3_584/index.html"
            },
            "created_at": "2025-11-10T08:04:47.565000"
        },
        {
            "id": "69119c8197046012e128f441",
            "product_url": "https://books.toscrape.com/catalogue/a-spys-devotion-the-regency-spies-of-london-1_3/index.html",
            "upc": "19fec36a1dfb4c16",
            "name": "A Spy's Devotion (The Regency Spies of London #1)",
            "description": "In England\u2019s Regency era, manners and elegance reign in public life\u2014but behind closed doors treason and tawdriness thrive. Nicholas Langdon is no stranger to reserved civility or bloody barbarity. After suffering a battlefield injury, the wealthy, well-connected British officer returns home to heal\u2014and to fulfill a dying soldier\u2019s last wish by delivering his coded diary.At In England\u2019s Regency era, manners and elegance reign in public life\u2014but behind closed doors treason and tawdriness thrive. Nicholas Langdon is no stranger to reserved civility or bloody barbarity. After suffering a battlefield injury, the wealthy, well-connected British officer returns home to heal\u2014and to fulfill a dying soldier\u2019s last wish by delivering his coded diary.At the home of the Wilherns, one of England\u2019s most powerful families, Langdon attends a lavish ball where he meets their beautiful and intelligent ward, Julia Grey. Determined to maintain propriety, he keeps his distance\u2014until the diary is stolen and all clues lead to Julia\u2019s guardian. As Langdon traces an evil plot that could be the nation\u2019s undoing, he grows ever more intrigued by the lovely young woman. And when Julia realizes that England\u2014and the man she is falling in love with\u2014need her help, she finds herself caught in the fray. Will the two succumb to their attraction while fighting to save their country? ...more",
            "category": "Historical Fiction",
            "price_incl_tax": 16.97,
            "price_excl_tax": 16.97,
            "availability": 1,
            "num_reviews": 0,
            "image_url": "https://books.toscrape.com/media/cache/f9/6b/f96b60a7614c4e3e868b82f6811efc7c.jpg",
            "rating": 5,
            "content_hash": "ddbb475fc04adf18f2546485b21a0e7bff43ca9484e308fde23c29ac7b1ea90d",
            "updated_at": "2025-11-10T08:04:17.195000",
            "crawl_meta": {
                "ts": "2025-11-10T08:04:17.195000",
                "status": "ok",
                "source_url": "https://books.toscrape.com/catalogue/a-spys-devotion-the-regency-spies-of-london-1_3/index.html"
            },
            "created_at": "2025-11-10T08:04:17.195000"
        }
    ]
}
(venv) ➜  Books-crawler git:(main) BOOK_ID=$(
  curl -s -H "X-API-Key: $API_KEY" "http://localhost:9010/books?page=1&page_size=1" \
  | python - <<'PY'
import sys, json
data=json.load(sys.stdin)
print(data["items"][0]["id"])
PY
)
echo "$BOOK_ID"

  File "<stdin>", line 1
    {"page":1,"page_size":1,"pages":402,"total":402,"items":[{"id":"69119bf92d95a6c0fb518484","product_url":"https://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html","upc":"a22124811bfa8350","name":"It's Only the Himalayas","description":"“Wherever you go, whatever you do, just . . . don’t do anything stupid.” —My MotherDuring her yearlong adventure backpacking from South Africa to Singapore, S. Bedford definitely did a few things her mother might classify as \"stupid.\" She swam with great white sharks in South Africa, ran from lions in Zimbabwe, climbed a Himalayan mountain without training in Nepal, and wa “Wherever you go, whatever you do, just . . . don’t do anything stupid.” —My MotherDuring her yearlong adventure backpacking from South Africa to Singapore, S. Bedford definitely did a few things her mother might classify as \"stupid.\" She swam with great white sharks in South Africa, ran from lions in Zimbabwe, climbed a Himalayan mountain without training in Nepal, and watched as her friend was attacked by a monkey in Indonesia.But interspersed in those slightly more crazy moments, Sue Bedfored and her friend \"Sara the Stoic\" experienced the sights, sounds, life, and culture of fifteen countries. Joined along the way by a few friends and their aging fathers here and there, Sue and Sara experience the trip of a lifetime. They fall in love with the world, cultivate an appreciation for home, and discover who, or what, they want to become.It's Only the Himalayas is the incredibly funny, sometimes outlandish, always entertaining confession of a young backpacker that will inspire you to take your own adventure. ...more","category":"Travel","price_incl_tax":45.17,"price_excl_tax":45.17,"availability":19,"num_reviews":0,"image_url":"https://books.toscrape.com/media/cache/6d/41/6d418a73cc7d4ecfd75ca11d854041db.jpg","rating":2,"content_hash":"1b629cc81963b0046d76dd1e3eff4714a64afb7e73f038c36c4170ca93a6b8e8","updated_at":"2025-11-10T08:02:01.054000","crawl_meta":{"ts":"2025-11-10T08:02:01.054000","status":"ok","source_url":"https://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html"},"created_at":"2025-11-10T08:02:01.054000"}]}import sys, json
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                