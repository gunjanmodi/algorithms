import json
agents = """

[
    {
        "pattern": "Acast",
        "name": "Acast",
        "slug": "acast.com",
        "url": "https:\/\/www.acast.com\/en",
        "acceptsaac": "0"
    },
    {
        "pattern": "Aggregator\/",
        "name": "Aggregator",
        "slug": "aggregator.tughi.github.io",
        "url": "https:\/\/tughi.github.io\/aggregator-android\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "AirPodcasts\/",
        "name": "AirPodcasts-unknown",
        "slug": "airpodcasts",
        "url": "",
        "acceptsaac": "0"
    },
    {
        "pattern": "Airr Podcatcher",
        "name": "Airr",
        "slug": "airr.io",
        "url": "https:\/\/www.airr.io\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "Amazon Music Podcast",
        "name": "Amazon Music Podcasts",
        "slug": "amazon.com",
        "url": "https:\/\/music.amazon.com\/podcasts\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "AntennaPod\/",
        "name": "AntennaPod",
        "slug": "antennapod.org",
        "url": "https:\/\/antennapod.org\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "anytime_podcast_player",
        "name": "Anytime podcast player",
        "slug": "anytime.amugofjava.me.uk",
        "url": "https:\/\/github.com\/amugofjava\/anytime_podcast_player",
        "acceptsaac": "0"
    },
    {
        "pattern": "iTunes\/",
        "name": "Apple iTunes",
        "slug": "itunes.apple.com",
        "url": "https:\/\/apple.com",
        "acceptsaac": "1"
    },
    {
        "pattern": "itunesstored\/1.0",
        "name": "Apple iTunes Store",
        "slug": "store.itunes.apple.com",
        "url": "",
        "acceptsaac": "1"
    },
    {
        "pattern": "Podcasts\/",
        "name": "Apple Podcasts",
        "slug": "podcasts.apple.com",
        "url": "https:\/\/apple.com",
        "acceptsaac": "1"
    },
    {
        "pattern": "iTMS",
        "name": "Apple Podcasts",
        "slug": "itms.apple.com",
        "url": "https:\/\/podcasts.apple.com\/",
        "acceptsaac": "1"
    },
    {
        "pattern": "Balados\/",
        "name": "Apple Podcasts",
        "slug": "podcasts.apple.com",
        "url": "https:\/\/apple.com",
        "acceptsaac": "1"
    },
    {
        "pattern": "Balados\/",
        "name": "Apple Podcasts",
        "slug": "podcasts.apple.com",
        "url": "https:\/\/apple.com",
        "acceptsaac": "1"
    },
    {
        "pattern": "Podcasti\/",
        "name": "Apple Podcasts",
        "slug": "podcasts.apple.com",
        "url": "https:\/\/apple.com",
        "acceptsaac": "1"
    },
    {
        "pattern": "Podcastit\/",
        "name": "Apple Podcasts",
        "slug": "podcasts.apple.com",
        "url": "https:\/\/apple.com",
        "acceptsaac": "1"
    },
    {
        "pattern": "Podcasturi\/",
        "name": "Apple Podcasts",
        "slug": "podcasts.apple.com",
        "url": "https:\/\/apple.com",
        "acceptsaac": "1"
    },
    {
        "pattern": "Podcasty\/",
        "name": "Apple Podcasts",
        "slug": "podcasts.apple.com",
        "url": "https:\/\/apple.com",
        "acceptsaac": "1"
    },
    {
        "pattern": "Podcast\u2019ler\/",
        "name": "Apple Podcasts",
        "slug": "podcasts.apple.com",
        "url": "https:\/\/apple.com",
        "acceptsaac": "1"
    },
    {
        "pattern": "Podkaster\/",
        "name": "Apple Podcasts",
        "slug": "podcasts.apple.com",
        "url": "https:\/\/apple.com",
        "acceptsaac": "1"
    },
    {
        "pattern": "Podcaster\/",
        "name": "Apple Podcasts",
        "slug": "podcasts.apple.com",
        "url": "https:\/\/apple.com",
        "acceptsaac": "1"
    },
    {
        "pattern": "Podcast\/",
        "name": "Apple Podcasts",
        "slug": "podcasts.apple.com",
        "url": "https:\/\/apple.com",
        "acceptsaac": "1"
    },
    {
        "pattern": "Podcastok\/",
        "name": "Apple Podcasts",
        "slug": "podcasts.apple.com",
        "url": "https:\/\/apple.com",
        "acceptsaac": "1"
    },
    {
        "pattern": "\u041f\u043e\u0434\u043a\u0430\u0441\u0442\u0438\/",
        "name": "Apple Podcasts",
        "slug": "podcasts.apple.com",
        "url": "https:\/\/apple.com",
        "acceptsaac": "1"
    },
    {
        "pattern": "\u041f\u043e\u0434\u043a\u0430\u0441\u0442\u044b\/",
        "name": "Apple Podcasts",
        "slug": "podcasts.apple.com",
        "url": "https:\/\/apple.com",
        "acceptsaac": "1"
    },
    {
        "pattern": "\u05e4\u05d5\u05d3\u05e7\u05d0\u05e1\u05d8\u05d9\u05dd\/",
        "name": "Apple Podcasts",
        "slug": "podcasts.apple.com",
        "url": "https:\/\/apple.com",
        "acceptsaac": "1"
    },
    {
        "pattern": "\u0627\u0644\u0628\u0648\u062f\u0643\u0627\u0633\u062a\/",
        "name": "Apple Podcasts",
        "slug": "podcasts.apple.com",
        "url": "https:\/\/apple.com",
        "acceptsaac": "1"
    },
    {
        "pattern": "\u092a\u0949\u0921\u0915\u093e\u0938\u094d\u091f\/",
        "name": "Apple Podcasts",
        "slug": "podcasts.apple.com",
        "url": "https:\/\/apple.com",
        "acceptsaac": "1"
    },
    {
        "pattern": "\u0e1e\u0e47\u0e2d\u0e14\u0e04\u0e32\u0e2a\u0e17\u0e4c\/",
        "name": "Apple Podcasts",
        "slug": "podcasts.apple.com",
        "url": "https:\/\/apple.com",
        "acceptsaac": "1"
    },
    {
        "pattern": "\u64ad\u5ba2\/",
        "name": "Apple Podcasts",
        "slug": "podcasts.apple.com",
        "url": "https:\/\/apple.com",
        "acceptsaac": "1"
    },
    {
        "pattern": "\ud31f\uce90\uc2a4\ud2b8\/",
        "name": "Apple Podcasts",
        "slug": "podcasts.apple.com",
        "url": "https:\/\/apple.com",
        "acceptsaac": "1"
    },
    {
        "pattern": "special_archiver",
        "name": "archive.org",
        "slug": "archive.org",
        "url": "http:\/\/www.archive.org\/details\/archive.org_bot",
        "acceptsaac": "0"
    },
    {
        "pattern": "BazQux\/",
        "name": "BazQux Reader",
        "slug": "com.bazqux",
        "url": "https:\/\/bazqux.com\/fetcher",
        "acceptsaac": "0"
    },
    {
        "pattern": "BeyondPod",
        "name": "BeyondPod",
        "slug": "beyondpod.mobi",
        "url": "http:\/\/www.beyondpod.mobi\/android\/index.htm",
        "acceptsaac": "0"
    },
    {
        "pattern": "bingbot\/",
        "name": "BingBot",
        "slug": "bing.com",
        "url": "http:\/\/www.bing.com\/bingbot.htm",
        "acceptsaac": "0"
    },
    {
        "pattern": "Bitcast\/",
        "name": "Bitcast",
        "slug": "bitcast.fm",
        "url": "https:\/\/bitcast.fm",
        "acceptsaac": "0"
    },
    {
        "pattern": "bitcastbot",
        "name": "Bitcast",
        "slug": "bitcast.fm",
        "url": "https:\/\/bitcast.fm\/crawling",
        "acceptsaac": "0"
    },
    {
        "pattern": "Blogtrottr\/",
        "name": "Blogtrottr",
        "slug": "com.blogtrottr",
        "url": "https:\/\/blogtrottr.com",
        "acceptsaac": "0"
    },
    {
        "pattern": "RawVoice Generator\/",
        "name": "Blubrry Podcasting",
        "slug": "blubrry.com",
        "url": "https:\/\/create.blubrry.com\/resources\/blubrry-podcast-directory\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "Breaker\/",
        "name": "Breaker",
        "slug": "breaker.audio",
        "url": "https:\/\/www.breaker.audio\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "anytime.amugofjava.me.uk",
        "name": "Breez",
        "slug": "technology.breez",
        "url": "https:\/\/breez.technology\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "briefings.fm",
        "name": "briefings.fm",
        "slug": "briefings.fm",
        "url": "http:\/\/briefings.fm\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "Bullhorn Server",
        "name": "Bullhorn",
        "slug": "bullhorn.fm",
        "url": "https:\/\/www.bullhorn.fm\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "Castbox",
        "name": "Castbox",
        "slug": "castbox.fm",
        "url": "https:\/\/castbox.fm\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "CastFeedValidator",
        "name": "CastFeedValidator",
        "slug": "castfeedvalidator",
        "url": "https:\/\/castfeedvalidator.com\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "Tentacles",
        "name": "Castro",
        "slug": "castro.fm",
        "url": "https:\/\/castro.fm\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "Mozilla\/5.0 +https:\/\/chartable.com\/crawler Trackable\/",
        "name": "Chartable",
        "slug": "chartable.com",
        "url": "https:\/\/chartable.com\/crawler",
        "acceptsaac": "0"
    },
    {
        "pattern": "Podcast-CriticalMention\/",
        "name": "Critical Mention",
        "slug": "criticalmention.com",
        "url": "https:\/\/www.criticalmention.com\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "Deezer Podcasters\/",
        "name": "Deezer",
        "slug": "deezer.com",
        "url": "https:\/\/www.deezer.com\/en\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "DEVONthink",
        "name": "DEVONthink",
        "slug": "devontechnologies.com",
        "url": "https:\/\/www.devontechnologies.com\/apps\/devonthink",
        "acceptsaac": "0"
    },
    {
        "pattern": "dlvr.it\/",
        "name": "dlvr.it",
        "slug": "com.dlvrit",
        "url": "https:\/\/dlvrit.com",
        "acceptsaac": "0"
    },
    {
        "pattern": "DoggCatcher",
        "name": "DoggCatcher",
        "slug": "doggcatcher.com",
        "url": "http:\/\/www.doggcatcher.com\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "Downcast\/",
        "name": "Downcast",
        "slug": "downcastapp.com",
        "url": "http:\/\/www.downcastapp.com\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "edgar",
        "name": "Edgar",
        "slug": "meetedgar.com",
        "url": "https:\/\/meetedgar.com\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "Entale bot",
        "name": "Entale",
        "slug": "entale.co",
        "url": "https:\/\/www.entale.co",
        "acceptsaac": "0"
    },
    {
        "pattern": "facebookexternalhit\/",
        "name": "Facebook",
        "slug": "com.facebook",
        "url": "https:\/\/www.facebook.com\/externalhit_uatext.php",
        "acceptsaac": "0"
    },
    {
        "pattern": "Feed Wrangler\/",
        "name": "Feed Wrangler",
        "slug": "feedwrangler.net",
        "url": "https:\/\/feedwrangler.net\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "Feedbin",
        "name": "Feedbin",
        "slug": "feedbin.com",
        "url": "https:\/\/feedbin.com\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "feeder.co",
        "name": "Feeder",
        "slug": "feeder.co",
        "url": "https:\/\/feeder.co\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "Feedly",
        "name": "Feedly",
        "slug": "feedly.com",
        "url": "https:\/\/feedly.com\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "Feedspot\/",
        "name": "Feedspot",
        "slug": "feedspot.com",
        "url": "https:\/\/www.feedspot.com\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "ffydpoll",
        "name": "Ffyd",
        "slug": "ffyd.de",
        "url": "https:\/\/fyyd.de\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "FreshRSS",
        "name": "FreshRSS",
        "slug": "freshrss.org",
        "url": "https:\/\/freshrss.org\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "Fusebox",
        "name": "Fusebox",
        "slug": "fm.fusebox",
        "url": "https:\/\/app.fusebox.fm",
        "acceptsaac": "0"
    },
    {
        "pattern": "FYEO\/",
        "name": "FYEO",
        "slug": "fyeo.de",
        "url": "https:\/\/www.fyeo.de",
        "acceptsaac": "0"
    },
    {
        "pattern": "fyyd\/",
        "name": "Fyyd",
        "slug": "fyyd.de",
        "url": "https:\/\/fyyd.de\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "fyyd-poll",
        "name": "Fyyd",
        "slug": "fyyd.de",
        "url": "https:\/\/fyyd.de\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "FeedFetcher-Google",
        "name": "Google Feedfetcher",
        "slug": "com.google.feedfetcher",
        "url": "http:\/\/www.google.com\/feedfetcher.html",
        "acceptsaac": "0"
    },
    {
        "pattern": "Googlebot",
        "name": "Google Podcasts and Search",
        "slug": "bot.google.com",
        "url": "https:\/\/www.google.com\/bot.html",
        "acceptsaac": "1"
    },
    {
        "pattern": "GEfektBot\/1",
        "name": "Govoren Efekt Bot",
        "slug": "govorenefekt.com",
        "url": "https:\/\/govorenefekt.com\/bot\/#english",
        "acceptsaac": "0"
    },
    {
        "pattern": "gPodder\/",
        "name": "gPodder",
        "slug": "gpodder.github.io",
        "url": "https:\/\/gpodder.github.io\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "hackney\/",
        "name": "Hackney-unknown",
        "slug": "hackney",
        "url": "",
        "acceptsaac": "0"
    },
    {
        "pattern": "Headliner",
        "name": "Headliner",
        "slug": "headliner.app",
        "url": "https:\/\/www.headliner.app\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "Hypefactors",
        "name": "Hypefactors",
        "slug": "hypefactors.com",
        "url": "https:\/\/app.hypefactors.com\/media-monitoring\/about.html",
        "acceptsaac": "0"
    },
    {
        "pattern": "Buck\/",
        "name": "Hypefactors",
        "slug": "hypefactors.com",
        "url": "https:\/\/app.hypefactors.com\/media-monitoring\/about.html",
        "acceptsaac": "0"
    },
    {
        "pattern": "iCatcher",
        "name": "iCatcher! Podcast Player",
        "slug": "joeisanerd.com",
        "url": "https:\/\/www.joeisanerd.com\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "Mozilla\/5.0 (Linux;) AppleWebKit\/ Chrome\/ Safari",
        "name": "iHeartRadio",
        "slug": "iheartradio.com",
        "url": "https:\/\/iheartradio.com",
        "acceptsaac": "0"
    },
    {
        "pattern": "inoreader.com",
        "name": "Inoreader",
        "slug": "inoreader.com",
        "url": "https:\/\/www.inoreader.com\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "Instacast\/",
        "name": "Instacast",
        "slug": "instacast",
        "url": "https:\/\/9to5mac.com\/guides\/instacast\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "iVoox",
        "name": "iVoox",
        "slug": "ivoox.com",
        "url": "https:\/\/www.ivoox.com\/en\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "Krzana bot",
        "name": "Krzana",
        "slug": "krzana.com",
        "url": "https:\/\/krzana.com\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "Leaf\/",
        "name": "Leaf-unknown",
        "slug": "leaf",
        "url": "",
        "acceptsaac": "0"
    },
    {
        "pattern": "life-radio-konsole-app",
        "name": "Life Radio Konsole App",
        "slug": "at.liferadio",
        "url": "https:\/\/www.liferadio.at\/life-radio-podcasts",
        "acceptsaac": "0"
    },
    {
        "pattern": "Liferea\/",
        "name": "Liferea",
        "slug": "liferea.lzone.de",
        "url": "https:\/\/lzone.de\/liferea\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "Lisnybot",
        "name": "Lisny",
        "slug": "com.lisny",
        "url": "https:\/\/www.lisny.com\/bot",
        "acceptsaac": "0"
    },
    {
        "pattern": "ListenAppBot",
        "name": "Listen App",
        "slug": "co.listenapp",
        "url": "https:\/\/listenapp.co",
        "acceptsaac": "0"
    },
    {
        "pattern": "ListenNotes",
        "name": "Listen Notes",
        "slug": "listennotes.com",
        "url": "https:\/\/www.listennotes.com\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "Luminary\/",
        "name": "Luminary",
        "slug": "luminary.com",
        "url": "https:\/\/luminarypodcasts.com\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "Micro.blog\/",
        "name": "Micro.blog",
        "slug": "micro.blog",
        "url": "https:\/\/micro.blog\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "MissinglettrBot\/",
        "name": "MissingLettr",
        "slug": "missinglettr.com",
        "url": "https:\/\/missinglettr.com\/bot\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "MuckRackFeedParser",
        "name": "Muck Rack",
        "slug": "muckrack.com",
        "url": "https:\/\/muckrack.com\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "NetNewsWire",
        "name": "NetNewsWire",
        "slug": "netnewswire.com",
        "url": "https:\/\/netnewswire.com\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "Netvibes",
        "name": "Netvibes",
        "slug": "netvibes.com",
        "url": "https:\/\/www.netvibes.com\/en",
        "acceptsaac": "0"
    },
    {
        "pattern": "News Explorer\/",
        "name": "News Explorer",
        "slug": "betamagic.nl",
        "url": "https:\/\/betamagic.nl\/products\/newsexplorer.html",
        "acceptsaac": "0"
    },
    {
        "pattern": "NewsBlur Feed Fetcher",
        "name": "NewsBlur",
        "slug": "newsblur.com",
        "url": "https:\/\/www.newsblur.com\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "Newsify Feed Fetcher",
        "name": "Newsify",
        "slug": "newsify.co",
        "url": "http:\/\/www.newsify.co\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "NextCloud-News\/",
        "name": "Nextcloud",
        "slug": "nextcloud.com",
        "url": "https:\/\/nextcloud.com\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "NRCAudioBot\/",
        "name": "NRC Audio",
        "slug": "audio.nrc.nl",
        "url": "https:\/\/www.nrc.nl\/audio\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "Office 365 Connectors",
        "name": "Office 365",
        "slug": "microsoft.com",
        "url": "https:\/\/microsoft.com",
        "acceptsaac": "0"
    },
    {
        "pattern": "Overcast\/",
        "name": "Overcast",
        "slug": "overcast.fm",
        "url": "https:\/\/overcast.fm\/",
        "acceptsaac": "1"
    },
    {
        "pattern": "OwlTail\/",
        "name": "OwlTail",
        "slug": "owltail.com",
        "url": "https:\/\/www.owltail.com\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "PandoraRSSCrawler",
        "name": "Pandora",
        "slug": "pandora.com",
        "url": "https:\/\/pandora.com",
        "acceptsaac": "0"
    },
    {
        "pattern": "PaperLiBot\/",
        "name": "Paper.li",
        "slug": "paper.li",
        "url": "https:\/\/paper.li\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "PetalBot",
        "name": "PetalBot",
        "slug": "com.petalsearch",
        "url": "https:\/\/webmaster.petalsearch.com\/site\/petalbot",
        "acceptsaac": "0"
    },
    {
        "pattern": "Playapod\/",
        "name": "Playapod",
        "slug": "playapod.com",
        "url": "https:\/\/playapod.com",
        "acceptsaac": "0"
    },
    {
        "pattern": "PlayerFM\/1.0 Podcast Sync",
        "name": "Player FM",
        "slug": "player.fm",
        "url": "https:\/\/player.fm\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "Plex\/",
        "name": "Plex",
        "slug": "plex.tv",
        "url": "https:\/\/www.plex.tv\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "plex",
        "name": "Plex",
        "slug": "plex.tv",
        "url": "https:\/\/www.plex.tv\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "Plex Media Providers",
        "name": "Plex",
        "slug": "plex.tv",
        "url": "https:\/\/www.plex.tv\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "PocketCasts\/",
        "name": "Pocket Casts",
        "slug": "pocketcasts.com",
        "url": "https:\/\/www.pocketcasts.com\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "Swoot\/",
        "name": "Pod Hero",
        "slug": "podhero.com",
        "url": "https:\/\/podhero.com\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "Mozilla\/5.0 (compatible; Podalong\/",
        "name": "Podalong",
        "slug": "podalong.com",
        "url": "https:\/\/www.podalong.com\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "Podbay\/",
        "name": "Podbay",
        "slug": "podbay.fm",
        "url": "https:\/\/podbay.fm\/about",
        "acceptsaac": "0"
    },
    {
        "pattern": "PodbeanFeedReader\/",
        "name": "Podbean",
        "slug": "podbean.com",
        "url": "https:\/\/www.podbean.com\/podcast-app-iphone-android-mobile",
        "acceptsaac": "0"
    },
    {
        "pattern": "PodcastGuru",
        "name": "Podcast Guru",
        "slug": "podcastguru.io",
        "url": "https:\/\/podcastguru.io\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "Podcastindex.org\/",
        "name": "Podcast Index",
        "slug": "podcastindex.org",
        "url": "https:\/\/podcastindex.org",
        "acceptsaac": "0"
    },
    {
        "pattern": "PodcastRepublic\/",
        "name": "Podcast Republic",
        "slug": "podcastrepublic.net",
        "url": "https:\/\/www.podcastrepublic.net\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "PodcastAddict\/",
        "name": "PodcastAddict",
        "slug": "podcastaddict.com",
        "url": "https:\/\/podcastaddict.com\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "Podcastly\/",
        "name": "Podcastly",
        "slug": "pdcstly.com",
        "url": "https:\/\/pdcstly.com\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "Podcastly\/",
        "name": "Podcastly",
        "slug": "pdcstly.com",
        "url": "https:\/\/pdcstly.com\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "PodcastScraper",
        "name": "PodcastScraper",
        "slug": "PodcastScraper",
        "url": "https:\/\/github.com\/jwhong\/PodcastScraper",
        "acceptsaac": "0"
    },
    {
        "pattern": "Podchaser-Parser",
        "name": "Podchaser",
        "slug": "podchaser.com",
        "url": "https:\/\/www.podchaser.com\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "podCloud\/",
        "name": "podCloud",
        "slug": "podcloud.fr",
        "url": "https:\/\/podcloud.fr\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "PodCruncher",
        "name": "PodCruncher",
        "slug": "podcruncher.co",
        "url": "https:\/\/podcruncher.co\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "PodEngine\/",
        "name": "PodEngine",
        "slug": "podengine.com",
        "url": "http:\/\/podengine.com",
        "acceptsaac": "0"
    },
    {
        "pattern": "podfollowbot\/",
        "name": "Podfollow",
        "slug": "podfollow.com",
        "url": "https:\/\/podfollow.com\/crawling",
        "acceptsaac": "0"
    },
    {
        "pattern": "PodheroBot\/",
        "name": "Podhero",
        "slug": "podhero.com",
        "url": "https:\/\/podhero.com\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "PodHound\/",
        "name": "PodHound",
        "slug": "podhound.co",
        "url": "https:\/\/podhound.co\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "Podimo\/",
        "name": "Podimo",
        "slug": "podimo.com",
        "url": "https:\/\/podimo.com\/en",
        "acceptsaac": "0"
    },
    {
        "pattern": "Podinstall",
        "name": "Podinstall",
        "slug": "podinstall.com",
        "url": "https:\/\/www.podinstall.com\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "Podkicker",
        "name": "Podkicker",
        "slug": "podkicker.com",
        "url": "https:\/\/www.podkicker.com\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "PodLink",
        "name": "PodLink",
        "slug": "pod.link",
        "url": "http:\/\/pod.link\/faq\/crawler",
        "acceptsaac": "0"
    },
    {
        "pattern": "PodBotLP\/",
        "name": "PodLP",
        "slug": "podlp.com",
        "url": "https:\/\/podlp.com",
        "acceptsaac": "0"
    },
    {
        "pattern": "PodMN\/",
        "name": "PodMN",
        "slug": "podmn.com",
        "url": "https:\/\/podmn.com",
        "acceptsaac": "0"
    },
    {
        "pattern": "PodMust\/",
        "name": "PodMust",
        "slug": "podmust.com",
        "url": "https:\/\/podmust.com",
        "acceptsaac": "0"
    },
    {
        "pattern": "Podmust\/",
        "name": "Podmust",
        "slug": "podmust.com",
        "url": "https:\/\/podmust.com\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "PodnewsBot",
        "name": "PodnewsBot",
        "slug": "podnews.net",
        "url": "https:\/\/podnews.net\/bot",
        "acceptsaac": "0"
    },
    {
        "pattern": "PodParadise",
        "name": "PodParadise",
        "slug": "podparadise.com",
        "url": "https:\/\/www.podparadise.com",
        "acceptsaac": "0"
    },
    {
        "pattern": "Podsights\/",
        "name": "Podsights",
        "slug": "podsights.com",
        "url": "https:\/\/podsights.com\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "Podtail\/",
        "name": "Podtail",
        "slug": "podtail.com",
        "url": "https:\/\/podtail.com\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "Mozilla\/5.0 (compatible; Podtail\/",
        "name": "Podtail",
        "slug": "podtail.com",
        "url": "https:\/\/podtail.com\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "podtail",
        "name": "Podtail",
        "slug": "podtail.com",
        "url": "https:\/\/podtail.com\/en\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "Podverse\/Feed Parser",
        "name": "Podverse",
        "slug": "podverse.fm",
        "url": "https:\/\/podverse.fm\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "Podyssey App",
        "name": "Podyssey App",
        "slug": "podyssey.fm",
        "url": "https:\/\/podyssey.fm",
        "acceptsaac": "0"
    },
    {
        "pattern": "Radical-Edward",
        "name": "Radical-Edward Podcast Discovery",
        "slug": "rheo.tv",
        "url": "https:\/\/rheo.tv\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "axios\/0.19.1",
        "name": "radio.com",
        "slug": "radio.com",
        "url": "https:\/\/www.radio.com\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "Radioline",
        "name": "Radioline",
        "slug": "radioline.co",
        "url": "https:\/\/www.radioline.co\/faq",
        "acceptsaac": "0"
    },
    {
        "pattern": "RadioPublic-Web\/",
        "name": "RadioPublic",
        "slug": "radiopublic.com",
        "url": "https:\/\/radiopublic.com\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "reason\/",
        "name": "Reason",
        "slug": "fm.reason",
        "url": "https:\/\/reason.fm\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "Reeder\/",
        "name": "Reeder",
        "slug": "reederapp.com",
        "url": "https:\/\/reederapp.com\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "Repod\/",
        "name": "Repod",
        "slug": "repod.io",
        "url": "https:\/\/repod.io\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "rssapi.net",
        "name": "RSS API",
        "slug": "net.rssapi",
        "url": "https:\/\/rssapi.net",
        "acceptsaac": "0"
    },
    {
        "pattern": "RSSOwl\/",
        "name": "RSSOwl",
        "slug": "rssowl.org",
        "url": "http:\/\/www.rssowl.org\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "RSSRadio",
        "name": "RSSRadio",
        "slug": "rssrad.io",
        "url": "http:\/\/rssrad.io\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "R6_FeedFetcher",
        "name": "Salesforce",
        "slug": "salesforce.com",
        "url": "https:\/\/www.salesforce.com\/products\/marketing-cloud\/social-media-marketing\/?mc=radian6",
        "acceptsaac": "0"
    },
    {
        "pattern": "semantic-visions.com",
        "name": "Semantic Visions",
        "slug": "semantic-visions.com",
        "url": "https:\/\/semantic-visions.com\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "SemrushBot",
        "name": "SEMrushBot",
        "slug": "semrush.com",
        "url": "https:\/\/www.semrush.com\/bot\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "SerendeputyBot\/",
        "name": "Serendeputy",
        "slug": "serendeputy.com",
        "url": "https:\/\/serendeputy.com\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "SismicsReaderBot",
        "name": "Sismics Reader",
        "slug": "sismics.com",
        "url": "https:\/\/www.sismics.com\/reader\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "Slackbot",
        "name": "Slackbot",
        "slug": "slack.com",
        "url": "https:\/\/api.slack.com\/robots",
        "acceptsaac": "0"
    },
    {
        "pattern": "SocialBeeAgent",
        "name": "SocialBeeAgent",
        "slug": "socialbee.io",
        "url": "https:\/\/socialbee.io\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "Sonnet\/",
        "name": "Sonnet",
        "slug": "sonnet.fm",
        "url": "https:\/\/sonnet.fm\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "Spotify\/",
        "name": "Spotify",
        "slug": "spotify.com",
        "url": "https:\/\/podcasters.spotify.com",
        "acceptsaac": "0"
    },
    {
        "pattern": "Spreaker\/",
        "name": "Spreaker",
        "slug": "spreaker.com",
        "url": "https:\/\/www.spreaker.com\/download",
        "acceptsaac": "0"
    },
    {
        "pattern": "StitcherBot",
        "name": "Stitcher",
        "slug": "stitcher.com",
        "url": "https:\/\/www.stitcher.com\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "Subcast\/",
        "name": "Subcast-unknown",
        "slug": "subcast.com",
        "url": "http:\/\/subcast.com\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "Superfeedr bot",
        "name": "Superfeedr",
        "slug": "superfeedr.com",
        "url": "https:\/\/superfeedr.com\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "TapTapes",
        "name": "Taptapes",
        "slug": "taptapes.com",
        "url": "https:\/\/www.taptapes.com\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "theoldreader.com",
        "name": "The Old Reader",
        "slug": "theoldreader.com",
        "url": "https:\/\/theoldreader.com\/home",
        "acceptsaac": "0"
    },
    {
        "pattern": "tweetedtimes.com",
        "name": "The Tweeted Times",
        "slug": "tweetedtimes.com",
        "url": "https:\/\/tweetedtimes.com\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "Tiny Tiny RSS",
        "name": "Tiny Tiny RSS",
        "slug": "tt-rss.org",
        "url": "https:\/\/tt-rss.org\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "TPA\/",
        "name": "TPA-unknown",
        "slug": "tpa",
        "url": "",
        "acceptsaac": "0"
    },
    {
        "pattern": "trendictionbot",
        "name": "Trendiction Bot",
        "slug": "com.trendiction",
        "url": "https:\/\/www.trendiction.com\/bot",
        "acceptsaac": "0"
    },
    {
        "pattern": "TuneInRssParser\/",
        "name": "TuneIn",
        "slug": "https:\/\/tunein.com\/",
        "url": "com.tunein",
        "acceptsaac": "0"
    },
    {
        "pattern": "um-IC\/",
        "name": "Ubermetrics",
        "slug": "ubermetrics-technologies.com",
        "url": "https:\/\/www.ubermetrics-technologies.com\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "itms",
        "name": "Unknown crawler, for testing",
        "slug": "com.unknown.ap",
        "url": "",
        "acceptsaac": "0"
    },
    {
        "pattern": "verbbot\/",
        "name": "Verb.fm",
        "slug": "verb.fm",
        "url": "https:\/\/verb.fm\/crawling",
        "acceptsaac": "0"
    },
    {
        "pattern": "VictorReader",
        "name": "Victor Reader",
        "slug": "humanwear.com",
        "url": "http:\/\/www.humanware.com\/microsite\/stream\/index.html",
        "acceptsaac": "0"
    },
    {
        "pattern": "Vienna\/",
        "name": "ViennaRSS",
        "slug": "vienna-rss.com",
        "url": "https:\/\/www.vienna-rss.com\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "VurblBot\/",
        "name": "Vurbl",
        "slug": "vurbl.com",
        "url": "https:\/\/vurbl.com",
        "acceptsaac": "0"
    },
    {
        "pattern": "Winds:",
        "name": "Winds",
        "slug": "getstream.io",
        "url": "https:\/\/getstream.io\/winds\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "russ(xiaoyuzhou)\/1.0",
        "name": "Xiao Yu Zhou",
        "slug": "xiaoyuzhoufm.com",
        "url": "https:\/\/www.xiaoyuzhoufm.com\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "Russ",
        "name": "Xiao Yu Zhou",
        "slug": "xiaoyuzhoufm.com",
        "url": "https:\/\/www.xiaoyuzhoufm.com\/",
        "acceptsaac": "0"
    },
    {
        "pattern": "YandexBot\/",
        "name": "YandexBot",
        "slug": "yandex.com",
        "url": "https:\/\/yandex.com",
        "acceptsaac": "0"
    },
    {
        "pattern": "Zapier",
        "name": "Zapier",
        "slug": "zapier.com",
        "url": "https:\/\/zapier.com",
        "acceptsaac": "0"
    },
    {
        "pattern": "ZoominfoBot",
        "name": "Zoominfo",
        "slug": "zoominfo.com",
        "url": "https:\/\/www.zoominfo.com\/about-zoominfo\/zoominfobot",
        "acceptsaac": "0"
    }
]


"""
def main(agents):
    agents = json.loads(agents)
    for agent in agents:
        print(agent['pattern'])




main(agents)