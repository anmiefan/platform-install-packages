%define prefix /opt/kaltura

Summary: Kaltura Open Source Video Platform 
Name: kaltura-html5lib
Version: v2.47
Release: 3
Epoch: 0 
License: AGPLv3+
Group: Server/Platform 
Source0: https://github.com/kaltura/mwEmbed/tarball/%{name}-%{version}.tar.gz 
Source1: simplePhpXMLProxy.php
Source2: kaltura-html5lib-v2.14.tar.gz
Source3: kaltura-html5lib-v2.37.tar.gz
Source4: kaltura-html5lib-v2.37.1.tar.gz
Source5: kaltura-html5lib-v2.38.3.tar.gz
Source6: kaltura-html5lib-v2.42.tar.gz
Source7: kaltura-html5lib-v2.44.tar.gz
Source8: kaltura-html5lib-v2.45.tar.gz
Source9: kaltura-html5lib-v2.45.1.tar.gz
Source10: kaltura-html5lib-v2.46.tar.gz

URL: https://github.com/kaltura/mwEmbed 
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
Requires: php, kaltura-base

%description
Kaltura is the world's first Open Source Online Video Platform, transforming the way people work, 
learn, and entertain using online video. 
The Kaltura platform empowers media applications with advanced video management, publishing, 
and monetization tools that increase their reach and monetization and simplify their video operations. 
Kaltura improves productivity and interaction among millions of employees by providing enterprises 
powerful online video tools for boosting internal knowledge sharing, training, and collaboration, 
and for more effective marketing. Kaltura offers next generation learning for millions of students and 
teachers by providing educational institutions disruptive online video solutions for improved teaching,
learning, and increased engagement across campuses and beyond. 
For more information visit: http://corp.kaltura.com, http://www.kaltura.org and http://www.html5video.org.

This package installs the Kaltura HTML5 library.

%prep
%setup -q 
tar zxf %{SOURCE2} -C %{_builddir}/
tar zxf %{SOURCE3} -C %{_builddir}/
tar zxf %{SOURCE4} -C %{_builddir}/
tar zxf %{SOURCE5} -C %{_builddir}/
tar zxf %{SOURCE6} -C %{_builddir}/
tar zxf %{SOURCE7} -C %{_builddir}/
tar zxf %{SOURCE8} -C %{_builddir}/
tar zxf %{SOURCE9} -C %{_builddir}/
tar zxf %{SOURCE10} -C %{_builddir}/

%install
mkdir -p $RPM_BUILD_ROOT%{prefix}/web/html5/html5lib
for i in v2.14  v2.37  v2.37.1  v2.38.3  v2.42  v2.44  v2.45  v2.45.1 v2.46 %{version};do
	rm -rf %{_builddir}/%{name}-$i/modules/Widevine
	cp -r %{_builddir}/%{name}-$i $RPM_BUILD_ROOT%{prefix}/web/html5/html5lib/$i
	cp %{SOURCE1} $RPM_BUILD_ROOT%{prefix}/web/html5/html5lib/$i/
	ln -sf %{prefix}/app/configurations/html5.php $RPM_BUILD_ROOT%{prefix}/web/html5/html5lib/$i/LocalSettings.php 
	mkdir $RPM_BUILD_ROOT%{prefix}/web/html5/html5lib/$i/cache
done
%clean
rm -rf %{buildroot}

%post
if [ "$1" = 2 ];then
	if [ -r /etc/kaltura.d/system.ini ];then
		. /etc/kaltura.d/system.ini
		echo 'update ui_conf set html5_url = "/html5/html5lib/%{version}/mwEmbedLoader.php" where html5_url like "%html5lib/v2.%mwEmbedLoader.php"'|mysql -h$DB1_HOST -u $SUPER_USER -p$SUPER_USER_PASSWD -P$DB1_PORT $DB1_NAME
	fi
fi
find /opt/kaltura/web/html5/html5lib -type d -name cache -exec chown -R 48 {} \; 

%postun

%files
%defattr(-, root, root, 0755)
%doc COPYING README.markdown 
%{prefix}/web/html5/html5lib
%config %{prefix}/web/html5/html5lib/%{version}/LocalSettings.KalturaPlatform.php

%changelog
* Wed Sep 7 2016 Jess Portnoy <jess.portnoy@kaltura.com> - v2.47-2
- Auto upgrade players ui conf to the latest version upon each upgrade

* Tue Sep 6 2016 David Bezemer <david.bezemer@kaltura.com> - v2.47-2
- remove obsolete old player versions
- add missing player versions

* Mon Sep 5 2016 Jess Portnoy <jess.portnoy@kaltura.com> - v2.47-1
- FEC-5898 - Set hls.js to be on by default
- SUP-8648 - Live stream doesn't play after the first click with thumbnail embed
- SUP-8683 - Player doesn't display caption files alphabetically
- SUP-8704 - Switching Flavors on HLSJS Playback Beahviour
- SUP-8724 - Hovering menu blocking info tab
- SUP-7848 - Enable DVR in Manual live streams

* Tue Aug 2 2016 Jess Portnoy <jess.portnoy@kaltura.com> - v2.46-1
- FEC-5691 - Chrome cast - Different events are sent when you activate casting via Google Cast or via Chromecast plugin
- FEC-5762 - Chrome cast - Kanalony - Event 99 is sent duplicated
- FEC-5773 - Chrome cast - Replay is not working in playlist with auto-continiue
- FEC-5586 - Support captions on chromecast
- FEC-5796 - Bug with 'monitorEvent' event
- SUP-8163 - iPad video issue when switvhing tabs
- FEC-5795 - Playlist: Scrubber jumps when choosing flavor selector after performing change media
- FEC-5794 - incorrect uDRM play manifest requested on Edge
- FEC-5792 - Mobile skin - Regression - captions is shown in both smart containers
- FEC-5792 - Mobile skin - Regression - captions is shown in both smart containers
- FEC-5791 - Mobile skin - custom style - plugin's name in smart container
- FEC-5790 - Mobile skin - Custom spinner is not shown on mobiles
- FEC-5768 - Native Android - Player with OTT skin is shown with big icons and not in their loacation
- FEM-592 - screen flashes when control bar appears and disappears or when clicking play button to replay playback
- FEM-595 - flavor selector icon is displayed on the playing video
- FEC-4618 - DFP pre-roll : Ad new page is not ed upon clicking on Ad in Android
- FEC-5777 - Mobile skin :Switch caption button is not presented
- FEC-5787 - Mobile skin - Playhead is too big when player has custom style
- FEC-5775 - Player flag button - flag menu is cut on horizontal display
- FEC-5723 - Native iOS - Incorrect end time of video while dragging till the end
- FEC-5737 - Watermark overlaps on the control bar on Lenovo Yoga tab
- FEC-5740 - Mobile skin - Unable to continue the AD, after you back from DFP's site
- FEC-5727 - Native iOS - Duration is shown at left top side when you click on any plugin
- FEC-5734 - Native iOS - Plugins in smart container are shown cut
- FEC-5730 - Native iOS -- Unable to Copy player URL from Share plugin on iPhone
- FEC-5767 - Mobile skin :Back button in the incorrect place
- FEC-5822 - Mobile skin - Audio entry destroys the player
- FEC-5809 - DFP: Lean more is not clickable on iPad
- FEC-5808 - Lecture capture: Time, Fullscreen btn & Stream selector are misaligned when video not played on android
- FEC-5807 - Vast with bumper: "Play" button appears after pre-roll during bumper on Android
- FEC-5768 - Native Android - Player with OTT skin is shown with big icons and not in their loacation
- FEC-5801 - DFP pre-roll with enabled controls - pause doesn't works during Ad
- FEC-5823 - Chromecast - Playhead is not moving when you seek in Pause state
- FEC-5820 - Chromecast - when video finishes to play, the Playhead has a gap of 3-4px
- FEC-5801 - DFP pre-roll with enabled controls - pause doesn't works during Ad
- FEC-5829 - Chromecast - playlist - back/foreword buttons appears on TV
- FEC-5809 - DFP: Lean more is not clickable on iPad
- FEC-5835 - Chromecast -DFP preroll - AD is not playing before the video (is playing after a video, as post roll)
- FEC-5847 - Add audio selector plugin to studio
- FEC-5835 - Chromecast -DFP preroll - AD is not playing before the video (is playing after a video, as post roll)
- FEC-5849 - Chromecast: receiver logo displayed over player area during playing from MAC
- FEC-5852 - Regression:Kaltura Live with DVR: DVR scrubber is shown at left side of a player on MS edge instead of right
- Chromecast ui/x
- Support studio mobile simulation mode
- Mobile skin disabled by default
- block video tag poster for user agent cordova SDK (mobile devices)

* Tue Jul 19 2016 Jess Portnoy <jess.portnoy@kaltura.com> - v2.45.1-1
- FEC-5792 - Mobile skin - Regression - captions is shown in both smart containers
- FEC-5792 - Mobile skin - Regression - captions is shown in both smart containers
- FEC-5791 - Mobile skin - custom style - plugin's name in smart container
- FEC-5790 - Mobile skin - Custom spinner is not shown on mobiles
- FEC-5768 - Native Android - Player with OTT skin is shown with big icons and not in their location
- FEM-592 - screen flashes when control bar appears and disappears or when clicking play button to replay playback
- FEM-595 - flavour selector icon is displayed on the playing video
- FEC-4618 - DFP pre-roll : Ad new page is not opened upon clicking on Ad in Android
- FEC-5777 - Mobile skin :Switch caption button is not presented
- FEC-5787 - Mobile skin - Playhead is too big when player has custom style
- FEC-5775 - Player flag button - flag menu is cut on horizontal display
- FEC-5723 - Native iOS - Incorrect end time of video while dragging till the end
- FEC-5737 - Watermark overlaps on the control bar on Lenovo Yoga tab
- FEC-5740 - Mobile skin - Unable to continue the AD, after you back from DFP's site
- FEC-5727 - Native iOS - Duration is shown at left top side when you click on any plugin
- FEC-5734 - Native iOS - Plugins in smart container are shown cut
- FEC-5730 - Native iOS -- Unable to Copy player URL from Share plugin on iPhone
- FEC-5767 - Mobile skin :Back button in the incorrect place

* Tue Jul 5 2016 Jess Portnoy <jess.portnoy@kaltura.com> - v2.45-1
- FEC-5525 - Chrome cast - Seek event (17) is thrown when you click on replay
- FEC-5527 - Chromecast - no events rare sent after replay
- FEC-5526 - Chromecast - Play_reached_50 and 75 is not thrown when you seek almost to the end of a video
- FEC-5615 - Youtube player on Android - current time not updating
- FEC-5582 - Channel playlist: ID 18-pre-roll ad is not playing before most video
- FEC-5282 - Mobile Skin Portrait Mode
- FEC-5310 - Mobile Skin Landscape Mode
- FEC-5503 - Add support for Related Plugin
- FEC-5505 - Add support for Playlists
- FEC-5506 - Add support for watermark plugin
- FEC-5508 - Add support for Watermarked HLS (Stream with KS)
- FEC-5509 - Support toggling cast from the browser Chromecast icon
- FEC-5510 - Add support for custom receiver logo
- FEC-5511 - Support sending proxyData to the receiver and custom proxyData
- SUP-8237
- FEC-5609 - Lecture capture (ID:40) - Unexpected black frame displays when in fullscreen
- FEC-5500 - Add Support for DFP Plugin
- FEC-5541 - youbora : error event is triggered twice
- FEC-5513 - ChromeCast : DVR is not working on Chromecast
- FEC-5616 - Chromecast - auto deployment
- FEC-5626 - Mobile skin - Share is not shown on iPhone while player has smart container
- FEC-5628 - Mobile skin - Captions can't be changed on Mobiles
- FEC-5631 - Mobile skin - When video finishes to play the duration of video is shown 0:01 instead of 3:33
- FEC-5632 - Mobile Skin - Back is not shown on Nexus 6
- FEC-5633 - Mobile Skin - playlist with dfp preroll - Duration of video is shown on left upper player's side on android
- FEC-5634 - Mobile Skin - Playlist - Fullscreen icon is shown on Duration, when you click on video from playlist
- FEC-5635 - Mobile Skin - info - description is cut
- FEC-5637 - Mobile Skin - Quality settings - are not saved
- FEC-5638 - Mobile skin - Captions - Settings screen is not automatically after updating it
- FEC-5641 - Mobile skin - Playlist - Settings screen is not blurred when you click on it on the end of video
- FEC-5642 - Mobile skin - Playlist - Player should be disabled when DFP is playing
- FEC-5645 - Mobile skin - Report plugin should be disabled when confirmation screen is open
- FEC-5648 - Mobile skin - Playlist should be disabled when you back from iPhone's native player and DFP is shown
- FEC-5646 - Add ability to specify legacy document modes in player embeds
- FEC-5565 - MultiAudioTracks: Video stuck and scrubber continues the progress in case of changing audio track after replay (Edge browser only)
- FEC-5564 - MultiAudioTracks:Video is playing without sound in case of changing language after continuing the video from pause (Edge Only)
- FEC-5647 - Fix vtt.js IE8 crash
- FEC-5651 - Mobile Skin - Play button is shown when share and info is open on iPhone
- FEC-5654 - Mobile skin - 'x' doesn't react on iPhone after filling out report
- FEC-5657 - Mobile skin - Live indicator icon shown as 'x' instead to be shown as red circle
- FEC-5656 - Mobile skin - DFP contrary to old skin DFP shows video's duration instead of DFP's duration
- FEC-5652 - MultiAudioTracks: Language is displayed twice (each language) after mid-roll
- FEC-5636 - Mobile skin - playlist - Next button is shown before Play button in hovering control player
- FEC-5653 - Mobile skin - Playbutton is shown with loading spinner
- FEC-5659 - Mobile Skin - captions and Quality settings are duplicated each time you choose new entry from playlist
- FEC-5662 - mobile skin: Basics (ID:75) - Overlapping issue with Report dropdown icon
- SUP-8053
- SUP-8323
- FEC-5663 - Lecture capture (ID:19) - Cannot focus on Search bar if played video before
- FEC-5667 - Lecture capture (ID:39) - Cannot switch view mode after playing from slide menu
- FEC-5674 - Mobile skin - Unable to drag till the end of a video
- FEC-5666 - Channel Playlist (ID:1) - Play/Pause button does not display for youtube entry
- FEC-5501 - Add support for Youbora Plugin
- FEC-5710 - Native iOS - info - Uploaded time and Views are blue and underlined, like if they were links
- FEC-5326 - spinner appear on PlayReady on the fly (emss) and clear ISM playback on full screen
- FEC-5707 - Mobile Skin - Landscape only - Cannot interact with control bar in fullscreen mode
- FEC-5716 - FairPlayOnSafari: Video is not playing
- FEC-5717 - Add support for OTT HLS FPS
- FEC-5702 - UI fixes
- FEC-5687 - Mobile skin - Long title is not cut on mobiles
- FEC-5658 - Mobile skin - player's icons are flickering when you you click on Next video in playlist
- FEC-5689 - Playlist with watermark - Tapping on the watermark does not open Kaltura site in a new tab
- FEC-5721 - Mobile skin - Learn more on DFP is not clickable on Android
- FEC-5728 - Native iOS - Play button is not shown when you close plugin (for example Report)
- FEC-5732 - Native iOS - Aditional second is added to the video if you drag till the end of video
- FEC-5735 - DoubleClick: audio is playing after pressing on skip (Edge+Safari)
- FEC-5591 - Monetization: Doubleclick (ID:45) - Skip message overlaps with the control bar
- FEC-5718 - after change media wrong params sent in media hit
- FEC-5502 - Add support for kAnalony Plugin
- FEC-5745 - Chrome cast - Video doesn't start automatically after DFP preroll
- FEC-5752 - Chrome cast - Black screen while changing videos via next button in playlist
- fix polyfill dependency name
- Fix naming convention issue with polyfills
- Mobile skin UI fixes
- HlsJs Peer5 support
- Fix scope issue
- support native SDK messaging from mobile web to work samelessly with the receiver
- Turn off mobile skin for this version

* Fri Jun 3 2016 Jess Portnoy <jess.portnoy@kaltura.com> - v2.44-1
- FEC-5518 - Expose PTS in HLS JS player
- SUP-8167
- FEC-5503 - Add support for Related Plugin
- SUP-7515
- SUP-6103
- FEC-5419 - Buffer, interruption,
- FEC-5549 - MultiAudioTracks: Select audio button disabled on Edge browser
- FEC-5548 - Add ability to pass captions array via external captions event
- FEM-460 - Handle Kaltura.OverrideLicneseURL in MobileSDK/EmbedPlayerNativeComponent
- FEC-484 - Version Tag
- FEC-5457 - expose new event for external full screen
- FEC-5395 - hlsjs- heartbeat: trackSessionStart event not reported when playing kaltura live with dvr
- FEC-5567 - uDRM:WVCENC:Video is stuck with wrong current time instead of playing after performing seek from the end of video to beginning
- SUP-7410
- FEC-5569 - uDRM: Rate selector is not working
- FEC-5573 - Add ‘ setKDPAttribute’ support for ‘visible’ property in controlBarContainer and topBarContainer
- FEC-5575 - Setting DASH source multiple times while in init state crashes playback
- FEM-385 - Android | Native sdk | Multi audio/Captions support
- FEC-3682 - live HLS: Each time player buffers, the latency increases
- FEM-514 - Fix Undefined index in mweApiGetLicenseData.php
- SUP-7804
- FEC-5282 - Mobile Skin Portrait Mode
- FEC-5595 - Monetization: Vast (ID:12): Video does not resume from the 15th second after ad is finished playing
- FEC-5583 - Lecture capture (ID:42) -Audio/Video doesn't start playing on clicking Slide/Chapter'
- FEC-5580 - Webvtt: "Loading text" is shown at left upper side of a player, when switching between languages
- FEC-5576 - webvtt: gap is shown instead to show the cue at most right side of a player
- FEC-5574 - webvtt: cue text tag is not working
- FEC-5556 - closedCaptions - redundant div is created in the DOM per each language
- FEC-5599 - HTML player not switching DRM videos
- WEBC-691 - As a producer I'd like to upload a slide deck via the webcasting application
- FEC-1246 - Create per-user agent top level css classes
- FEC-5601 - HLS JS: Lecture Capture: Video starts from the beginning after changing stream
- FEC-5604 - changing the volume manually from x to 0, and click unmute, doesn't do anything
- FEC-5611 - Multiple Playlist: Monetization (ID:10) - Overlay Ad duration is not 5 seconds
- FEC-5602 - hlsjs: playlist with dfp - playback get stuck when playback switches from first to second entry
- SUP-8326
- SUP-8313
- updated resources page linking to VPASS
- fix xss
- Fix IOS resume playback after midroll ad
- Fix support for HLS AES as DRM source
- Update DASH everywhere package to v4.1.1
- updated Chromecast application ID in all test pages
- Add captions force webVTT flag for kaltura API on-the-fly generated webvtt captions

* Sun May 8 2016 Jess Portnoy <jess.portnoy@kaltura.com> - v2.43-1
- FEC-5259 - Set Doubleclick request ads timeout check only when play start
- FEC-4430 - Related videos with auto continue - each entry plays twice
- FEC-4992 - Related video: First entry is looped after all videos has been played
- SUP-7211 - Progress Bar color on iOS SDK
- FEC-5376 - Update Youbora Plugin to cover passing bitrate in all playback contexts
- OPF-4120 - Report CDN to youbora
- SUP-7693 - Typo in KMC studio Enable embed.ly embeds
- FEC-5129 - LC Dual screen: the dual screen menu appears over moderation screen
- FEC-5353 - kanalony: change service name and action name
- FEC-5292 - kanalony: remove "event:" from events names
- FEC-5271 - LC Dual screen: playlist with LC entry - spinner appears during first entry playing on Edge
- SUP-7573 - 3gp behvior
- FEM-432 - seek after EOF, player stuck
- FEC-5390 - When doubleclick leads with flash the timeout of adtag loading is not respected
- SUP-7662 - Player not displaying "Currently not broadcasting" message on mobile
- SUP-6103 - Chapters module embed code not working properly
- FEC-5404 - Javascript VPAID ad do not load using doubleClick plugin and player is stuck
- FEC-5267 - kanalony: Event type 3 (play) is fired only for the first entry in the playlist
- FEC-5293 - kanalony: flavourId should be added to all events as it is a required param
- FEC-5305 - kanalony: after watching vast or dfp postroll : player doesn't stop reporting Event 99 (viewing) every 10 seconds
- FEC-5269 - kanalony: Event 99 : playing content appears after event 14 – 100% content
- FEC-5307 - kanalony: quarterly events are not reported after replay. all other events are reported
- OPF-3749 - When the moveing playhead backward the subtitles not shown
- SUP-7493 - Issues with pixelation during playback
- FEC-4805 - failover doesn't work
- FEC-4907 - HLS-OSMF: external stream plays not smooth in first 15-20 seconds (only at the beginning)
- FEC-5115 - Add support for ID3 tags in HLS JS
- FEC-5308 - kanalonly: 50% and 75% quarterly events are not fired when user does seek
- SUP-6927 - Audio thumbnail display issues.
- FEC-5436 - universal stream doesn't play with hlsJS
- OPF-3862 - HD button is disable after clicking on continue button - Chrome only
- FEC-5335 - kanalony: position resets on ios during ads playback, unlike pc
- FEC-5278 - Two events from type 1 fired for smoothStreaming playback
- SUP-7673 - Adobe Heartbeat Integration
- SUP-7824 - Player does not save 'Button Size' settings
- FEC-5355 - IE edge: error appears in console - id3Tag :: ERROR :: TypeError: Unable to get property 'data' of undefined or null reference
- FEC-5438 - mediaLoaded event not fired after changing media
- SUP-7960 - onAdError: AdError 1009: The VAST response with cuePoints
- FEC-5245 - HLS JS: The First/Next entry in the playlist with Ads doesn't play on click
- FEC-5474 - MultiDRM + DoubleClick preroll - Source Selector doesn't show flavours
- FEC-5459 - HLS JS : Regression: VOD with Flavor selector is not working
- FEC-5458 - Rate selector - is not possible to change the playback speed on Microsoft Edge
- FEC-5485 - Seek from position 0 fails on Microsoft EDGE
- FEC-5484 - Force HLS Native playback for Microsoft EDGE
- TR-976 - Omniture calls aren't sent after hitting 'Replay' button on player timeline
- FEC-5444 - Silverlight: Flavor Selector: Flavors are not displayed in SPlayer (only auto)
- SUP-8040 - Media plays with ad and seek bar issue on FF
- FEC-4714 - ChromeCast - Live is not playing. Black screen is shown (Without Chrome cast the stream plays)
- FEC-5486 - ChromeCast - Chromecast thumbnail is not centralized in Fullscreen mode
- FEC-5476 - Playlist with Vast pre-roll: the playlist switched to enabled after click on Ad and return to the player
- FEC-5471 - Multiple Playlist: Pre-roll Ad is not played before the video start on iPhone
- FEC-5468 - Share&Embed: a video is not blurred on clicking 'Share'
- FEC-4725 - ChromeCast: player stack when you Stop casting from the middle of a video
- FEC-5494 - HLS JS : Only auto displayed after opening flavor selector when playing VOD/Live entry with multiple bitrates (IE11 Only)
- SUP-7729 - Frames of Kaltura Secret protected videos are visible to unauthenticated user
- FEC-5482 - MultiAudioTracks: Active language should be highlighted after opening "Select audio" button
- SUP-7780 - IVQ - Quitting before editing a new quiz creates a non functioning quiz in My Media
- FEC-5381 - webcast-sometimes after stop/start when changing the player view the video doesn't display
- FEC-5514 - Chromecast - Analytics - Only Seek event is shown
- FEC-5512 - Chrome cast - when you unpause Live entry, it doesn't back to Live
- FEC-5439 - player doesn't play according to mediaPlayFrom/mediaPlayTo - stuck with buffering wheel
- FEC-5524 - PlayReady is not working on IE11 (black screen with loading spinner )
- FEC-5191 - DVR Layout - Drag the scrabbler to the most right place doesn't return to live
- Fix HLS AES source selection for DRM allowed sources
- new HLS-OSMF plugin
- Chromecast support in android SDK
- add support for custom receiver logo url in Chromecast
- Update HLS.JS to v0.6.1 Add version print out when in debug mode*

* Sun Apr 10 2016 Jess Portnoy <jess.portnoy@kaltura.com> - v2.42-1
- FEC-4777 - Updated DVR Layout for Player
- SUP-7499 - duplicated countdown on ads
- FEC-4123 - can't select related video to play during an entry playback
- FEC-3806 - Playhead - Endless loading icon after press 'End' key on keyboard on Microsoft Edge
- FEC-4879 - Elapsed PTS doesn't work
- FEC-5056 - AdClicked dispatched only once
- FEC-4308 - Player mobile skin OPEN
- FEC-4938 - Multidrm playback engine - Media replays when it should end and stop
- TR-768 - Captions parameter displayCaptions is not respected with 2nd entry v2.41
- FEC-4811 - Integrate HLS-JS Plugin
- FEC-5098 - Integrate FPS service in player
- WEBC-712 - multicast - slide sync doesn't always work
- FEC-4893 - hls is not chosen on iPhone - Forgeahead Solutions Customer
- FEC-4576 - Playback- Movie cannot be played again if user clicks on back button
- FEC-5159 - Share - Items are left side aligned
- FEC-5160 - bitrate selector is enabled while is rotating , instead to stay disabled
- WEBC-712 - multicast - slide sync doesn't always work
- FEC-4833 - Load player once for all media
- FEC-4917 - Update DFP plugin so that the IMA SDK is not loaded on each new request with a new timestamp
- FEC-5189 - HLSjs: Kaltura Live: Off air appears when live is playing
- FEC-5187 - HLSjs: Kaltura Live: Play after pause is not working
- FEC-5186 - HLSjs: Kaltura Live with DVR is not playing smothly
- FEC-5183 - FairPlay for iOS fixes
- WEBC-679 - As a producer I'd like to select for all viewers the view setup at any point during the broadcast
- FEC-5190 - kaltura stats: play event is not fired for the second and third entry in a playlist with flash dfp
- FEC-5188 - yubora: 2 stop events are fired at the end of entry playback in a playlist
- SUP-7442 - Player - infoscreen doesn't
- WEBC-713 - webcast in Multicast - after disconnection of the video the player play the last 3 minutes in endless loop
- SUP-6501 - Capturespace presentation ratio
- SUP-7247 - Player - 2.39 - click twice to start live stream (thumbnail)
- SUP-6927 - Audio thumbnail display issues.
- FEC-5240 - Using tvpapiContinueToTime event when autoPlay is turning on.
- FEC-4894 - setting mediaPlayFrom to be greater than zero
- FEC-5250 - Add cache to multiDrm player assets
- FEC-5248 - not receiving concurrent notification
- FEC-5211 - HLSjs: Flavor selector doesn't not appear on player in case of playing live entries
- FEC-5253 - playlist auto-continue doesn't work (flash)
- FEC-3806 - Playhead - Endless loading icon after press 'End' key on keyboard on Microsoft Edge
- FEC-5279 - uDRM: Regression:Video with PlayReady with Dash Plugin is not playing
- FEC-5161 - CLONE - For each action shown two MediaMark
- FEC-5180 - DRM - player plays only audio with black video when performing doSeek after playerReady event
- FEC-5228 - Eternal loader is displayed after seeking from replay state
- FEC-5212 - Eternal spinner while Seek without pressing on Play
- FEC-5216 - Player doesn't play from last seek position
- FEC-5261 - Muted video plays with sound
- FEC-5227 - Bug reported from test: Switch media - Sometimes an error occurred while attempting to play video
- FEC-5229 - Bug reported from test: Volume control - Volume indicator is missing
- FEC-5262 - Seek bar is not hidden
- SUP-7442 - Player - infoscreen doesn't
- SUP-6501 - Capturespace presentation ratio
- FEC-5281 - Regression:uDRM:PlayReady:Video always starts to play automatically when big player button appears in the middle of player area
- FEC-5303 - Webcast VOD - slides doesn't appear in the player
- KMS-11206 - In-Video Quizzes: Embed: question skipped and wasn't jumped up on the defined time (after submission)
- FEC-5361 - Regression - DFP preroll is playing only at first entry in horizontal playlist
- KMS-11329 - Channel Playlist - When switching back to Capture space - Slide menu Stuck on regular videos
- KMS-11324 - Capturespace entries palyback does not work as expected in channel playlist
- FEC-4508 - Playlist with Live entry: if select any entry during Live playing, it failed to be play
- FEC-5249 - VOD and live entries in a playlist: Playlist is not loading
- support trafficking parameters in DoubleClick onAdPlay event
- new HLS-OSMF plugin
* Fri Mar 11 2016 Jess Portnoy <jess.portnoy@kaltura.com> - v2.41-1
- FEC-4777 - Updated DVR Layout for Player
- SUP-7065 - Content Drop-off - Play-through Ratio 121%
- OPF-2109 - HD and Bitrate bar not working on IE11 and EDGE
- OPF-2146 - player - the bar does not disappear when choosing audio langauge
- FEC-4801 - DoubleClick: onAdPlay event doesn't return the same parameters when using leadWithFlash is true and false
- FEC-4791 - Set DFP plugin to default to lead with html5 from player version 2.41
- FEC-4768 - DFP pre-roll: Playlist is not disabled when pre-roll ad paused
- FEC-4816 - MediaReady in dash-player
- OPF-2364 - Self-Care-Web/Player/Progress bar/Sometimes the progress bar doesn't work properly
- OPF-3047 - Self-Care-Web/Linear/The default audio language is English
- OPF-3033 - Self-Care-Web/Linear/ Playback is stopped before 15 minutes
- FEC-4400 - app crashes when starting to play media with postroll with fatal exception
- FEC-4838 - Ads started to play with audio only for several seconds on iPad
- FEC-4841 - DFP overlay: the player doesn't started to play, spinner appears all time
- FEC-4846 - Yubora: the code in the ping request is incorrect when playing a playlist
- FEC-4848 - attach buffering support on mwembed - web layer
- FEC-4852 - Playlist with DFP overlay: Play button appears during a video playing (flash player)
- FEC-4584 - Omniture do not dispatch segments-views after pause
- FEC-4859 - yubora: ping requests are not reported after replay
- FEC-4873 - regression: error messages appear for 2 seconds and then disappear
- FEC-4858 - yubora: bitrate of live streams is set incorrectly to -1 instead of the real bitrate
- FEC-4862 - yubora: the bitrate in ping events doens't update for hds/hls/akamai , but only to progressive download
- FEC-4860 - yubora: play and pause events are not reported for live stream
- PLAT-3728 - Anonymous user support WAITING FOR QA REVIEW
- SUP-6930 - O'Reilly Media - Audio only flavors are labeled as 240P
- FEC-4848 - attach buffering support on mwembed - web layer
- FEC-4860 - yubora: play and pause events are not reported for live stream
- FEC-4875 - yubora: bitrate equals to -1 in the first entry of the playlist
- FEC-4814 - Calling doPause right after doPlay is not pausing the video
- FEC-4882 - regression: playlist playback get stuck after playback of an ad that fails.
- FEC-4884 - HLS-OSMF: flash errors appear in IE browser
- FEC-4883 - HLS-OSMF: Black screen displayed during seek
- FEC-4358 - live multi-track audio, audio is played before video
- FEC-4609 - HLS-OSMF: stream stuck after limit bandwidth and no released after the limit disabled
- FEC-4482 - HLS OSMF - external stream stuck in limit the bandwidth to 0.5M
- FEC-4886 - MediaMark KPlayerEvenet returns "MediaMark" as the param
- FEC-4888 - regression: playback start with audio only on pc when adErrorEvent occurs
- FEC-4890 - yubora: two "data" requests sent when launching player with native app.
- FEC-4895 - yubora - there are errors that don't trigger the "error" event
- FEC-4658 - webcast live - Switching views in player is not smooth
- WEBC-686 - As an attendee I'd like to see view switches in a smooth and uninterrupted manner
- FEC-4901 - regression: comScoreStreamingTag- setCLip event not called
- FEC-4900 - regression: comscore doesn't fire events on a page with a playlist
- FEC-4852 - Playlist with DFP overlay: Play button appears during a video playing (flash player)
- FEC-4908 - double call to "notifyJsReady" - breaks "addKPlayerEventListener" on UIWebView
- FEC-4926 - Overlay Ad does not appear
- FEC-4813 - Social Sharing Links Do Not Pass Time Offset to Facebook/Twitter/LinkedIn/etc.
- FEC-3934 - Skip button doesn't work When using javascript (flash disabled) after switching media
- FEC-4947 - DFP Trafficking - Ads are not displayed
- FEC-4942 - DFP post-roll - Video is not getting played after tapping on Play button in iPad
- FEC-4945 - regression google analytics: midSequenceStart is fired without midSequenceComplete
- FEC-4903 - Vertical playlist with DFP becomes disabled after clicking on ad twice
- FEC-4915 - DFP Post roll: Ad is not Paused at first click
- FEC-4802 - Pass ad title in Doubleclick onAdPlay event
- SUP-7422 - DFP issue - "learn more' button isn't clickable.
- FEC-4957 - Live entry with adstiching plays with blackscreen on devices
- FEC-4941 - Not regression: DFP - preroll is not shown if you choose the video from playlist
- FEC-4939 - Regression: DFP pre-mid-post : you should press twice for replaying the entry in playlist
- FEC-4928 - DFP pre-mid-post : video stack and preroll is not shown on second video from related videos
- FEC-4928 - DFP pre-mid-post : video stack and preroll is not shown on second video from related videos
- FEC-4941 - Not regression: DFP - preroll is not shown if you choose the video from playlist
- FEC-4983 - Adding skip event
- FEC-5008 - Regression: comScore: Extra playback event fired for playback of dfp pre-roll
- FEC-5007 - Regression: Player api: "ad start: preroll" is fired for overlay
- FEC-4945 - regression google analytics: midSequenceStart is fired without midSequenceComplete
- FEC-5003 - V18 - Change media does not work
- FEC-5004 - V18 - Taping on screen, makes the screen blue for a fraction of second
- FEC-5010 - V18 - Taping on screen several times cause the player controls to disappear
- FEC-5003 - V18 - Change media does not work
- FEC-4970 - regression: omniture - milestones events are not reported in the right timing
- FEC-5028 - playback]Catchup: time point in tooltip is not align to the center
- FEC-5065 - Regression - Playlist is not getting disabled while midroll is playing
- FEC-5064 - DFP pre-mid-post: post-roll doesn't playing on iPad
- FEC-5061 - iOS trailer: 'Play' button is displayed on the screen only when pressing on it
- FEC-5057 - DFP - Scroll bar is flickering If you seek on after midroll place
- FEC-5051 - DFP pre-mid_post with playlist: nothing occurred after tap on big Play button in middle - iPad
- FEC-5049 - regression: heartbeat: trackVideoLoad and trackSessionStart events come before the ad play event on the second entry
- FEC-5046 - regression: playerPlayed and doPause events are fired between ad events
- FEC-5008 - Regression: comScore: Extra playback event fired for playback of dfp pre-roll
- FEC-4986 - Trailer not showing play button on iPhone
- FEC-5070 - uDRM:Regression: PlayReady with ForceDash: Scrubber stuck and video is playing with loading spinner after clicking on play button
- New HLS-OSMF plugin
- Fix decimal point issues in different culture settings of systems in silverlight*

* Sun Feb 14 2016 Jess Portnoy <jess.portnoy@kaltura.com> - v2.40-1
- FEC-4659 - webcast live - clicking pause/play, the player jumps back a few seconds
- FEC-4471 - HLS OSMF - external stream stuck during manual throttling
- FEC-4629 - Supporting Multi Track Audio on Safari via leveraging Safari API for audio
- FEC-4673 - Support load for Silverlight player DONE
- PLAT-4681 - Events Collection | Player Plugin Creation
- FEC-4690 - Develop Youbora Player Plugin
- Update DASH lib with LIVE playback fixes
- SUP-7026 - Related videos big thumbnail stretch
- SUP-6945 - Media plays before the ad
- FEC-4728 - Douleclick ads don't play on Android playlist
- FEC-4711 - Channel Playlist with Quiz: Playlist doesnt support quiz
- FEC-4580 - Enhanced Advertising > Content playback flow for web
- SUP-6930 - Audio only flavors are labeled as 240P
- SUP-6673 - Pause / play button doesn't work in playlist - switchOnResize
- SUP-6708 - Switch on Resize, full-screen & live entries on mobile no playback
- FEC-4735 - Playlist with Vast pre-roll: the ad doesn't started to play, stuck at beginning on Android
- FEC-4734 - regression: auto continue in playlist doesn't work. playback stops after transition from first to second entry
- FEC-4659 - webcast live - clicking pause/play, the player jumps back a few seconds
- Fix event flow after change media
- Doubleclick - Fallback to Flash on Microsoft Edge
- KMS-10787 - In-Video Quizzes: Channel playlist - 'almost done' screen is not shown
- FEC-4580 - Enhanced Advertising > Content playback flow for web
- FEC-4541 - update API documentation in player.kaltura.com documentation
- FEC-4475 - player iOS SDK throws error when loading an image entry
- FEC-4723 - Allow player to select dash+widevine on Android
- SUP-7123 - Layout of the play-button has been changed in the new version
- FEC-4674 - Support load for DRM player DONE
- FEC-4741 - Add support for offline OTT content
- FEC-4786 - In-Video Quizzes: Channel playlist - last question pops up - in case of seek via scrubber (YouTube)
- TR-196 - It is possible for a user to remove share link permanently (for the session at least)
- SUP-7156 - Playback issues with Embed Code

* Sun Jan 17 2016 Jess Portnoy <jess.portnoy@kaltura.com> - v2.39-1
- FEC-4308 - Player mobile skin
- FEC-4512 - Mobile Skin - Long Title is cut on portrait mode
- FEC-4511 - Mobile skin - Related videos shows settings icon on video while one entry has AC free preview
- FEC-4488 - Mobile Skin - Player is disoriented on iPhone while using native menu of iphone
- FEC-4524 - Webcast NO DVR- player freeze for 10 sec when
- FEC-3608 - Related Videos - Videos are cut after closing and reing Related plugin
- FEC-4525 - webcast (NO DVR) slide sync - slides arrived 15-20 second earlier
- FEC-4454 - webcast with no DVR - slides don't change on IE browser
- FEC-4453 - webcast - future slides appear in the slide menu
- TR-552 - CaaS widgets with playlist - On iOS thumbnail is out of alignment
- FEC-4550 - Mobile skin: moderation text outstanding from the box area
- FEC-4547 - Customized info: no close button appears for Info screen
- FEC-4510 - Mobile Skin - custom style brakes player on mobile
- SUP-6115 - Apple Voice over not working with thumbnail emebd
- SUP-6782 - inquiry as to mobile thumbnail embed - number of clicks to start a video
- FEC-4555 - Mobile Skin - Related video: replay button disabled after an entry finished
- FEC-4552 - Mobile Skin - Related videos - Play Button and spinner is shown at same time
- FEC-4549 - Mobile Skin - Overly is shown on control bar
- FEC-4544 - Mobile Skin - OTT skin in fullscreen mode shows control bar cut
- FEC-4538 - Mobile Skin - Playhead is not shown on the beginning of a progress bar
- FEC-4540 - Mobile Skin - HLS server side rate selector has wrong default value
- FEC-4535 - Mobile skin - control bar is cut after using native mobiles select box ( captions/Moderation)
- FEC-4543 - Mobile Skin - disables large play button while player has an auto loop
- FEC-4539 - Mobile Skin - When player has custom style smart containers are shown even if you don't have plugins in a player
- FEC-4542 - Info plugin: The info data doesn't re-sized in full screen mode
- FEC-3608 - Related Videos - Videos are cut after closing and reing Related plugin
- PLAT-4866 - webcast -last 10 sec of video is missing from the live event .
- FEC-4455 - ID3 tag sync - changing slides less than three seconds cause that the second slide don't appear
- FEC-4573 - DRM playback: after refreshing test page ,the replay doesn't works properly on FF
- FEC-4575 - Mobile Skin: Clicking on play button disables share (share was ed before)
- FEC-4465 - High cpu usage when there are many slides (>30)
- FEC-4456 - HLS OSMF - the spinner appears during DVR playing if to stop and re-run Kaltura stream
- FEC-4459 - HLS OSMF - take around 10-12 seconds to switch from DVR to Kaltura Live
- FEC-4462 - HLS OSMF - Seek in Kaltura DVR take more time than in previous player version
- FEC-4458 - HLS OSMF - Kaltura Live with DVR loaded with 40-50 seconds of delay
- FEC-4567 - Regression: Kaltura Live without DVR stuck at beginning for 10-15 second
- WEBC-632 - Use the creation time for answer-on-air instead of relative time
- FEC-4460 - HLS OSMF - the Kaltura live's time isn't synchronized with the timer - 1 minute difference
- FEC-4457 - HLS OSMF - After Kaltura Live stopped, the DVR started from 1 minute
- FEC-4452 - HLS OSMF - the DVR timer of the Kaltura live stopped to update after several seconds
- FEC-4451 - HLS OSMF - the timer for Kaltura live isn't updated
- FEC-4582 - Playlist with moderation: if select other entry during moderation screen ed ,the video blurred
- FEC-4536 - Mobile Skin - Multi streams box is located in center of a player
- FEC-4596 - Regression: empty playlist in full screen mode displayed on the half of the screen
- WEBC-644 - webcast embed - cancel button isn't in the right place (and fonts are wrong)
- FEC-4471 - HLS OSMF - external stream (WhetherNation) stuck during manual throttling
- FEC-4581 - It takes too long to start playing live (HLS)
- FEC-4594 - HLS OSMF - Kaltura Live without DVR and VOD periodically stuck for 2-3 seconds during throttling
- FEC-4612 - mac/iPad - after preforming stop/start in the encoder the video doesn't return until refresh the page
- FEC-4611 - embed webcast - the message on the player when on off air mode is cut due to QnA
- KMS-9595 - In Video Quizzes: Seek to the end of video via end button is not working in HDS (playhead continue to play and cue-points are not pop-upped)
- SUP-6931 - Support for inlineScripting RESOLVED
- KMS-9632 - In Video Quizzes: General: Skip for now is hidden in case of showing question when plugin option list is ed
- FEC-4615 - session Android and iOS
- SUP-6773 - Kaltura player v2.36.2 - live stream with pre-roll ads mixed audio
- KMS-9871 - In Video Quizzes: Player puts different questions on the same cue-point after seek from pause (causes to add few questions in one cuepoint)(youtube entry)
- FEC-4645 - Hidden Playlist - Next/Previous buttons not display during video playing on iPad
- FEC-4638 - Vertical responsive playlist distorted after the browser resized
- FEC-4636 - Lecture capture: Duration time works for first chapter only
- FEC-4630 - Share&Embed and LC - Share screen is unexpectedly when player stared to play on Android
- FEC-4352 - CaptureSpace - scrubber does not move and spinner stuck on the player (MAC only)
- FEC-4669 - double play on native component READY FOR MERGE
- FEC-4612 - mac/iPad - after preforming stop/start in the encoder the video doesn't return until refresh the page
- SUP-6647 - alert-container text overflows
- FEC-4664 - webcast iPad/ mac - slides doesn't appear in the menu slides
- FEC-4580 - Enhanced Advertising > Content playback flow for web READY FOR DEV
- SUP-6765 - Player does not end playback properly
- SUP-6906 - Cursor remains hidden after exiting fullscreen
- FEC-4660 - webcast on mac / ipad - after stop start the slides doesn't change
- SUP-6442 - Playlist player overflow in IPHONE 6+
- SUP-6927 - Audio thumbnail display issues.
- SUP-6143 - Player v2.35 - Icons Display
- FEC-4657 - Player seeks when changing audio stream
- FEC-4666 - autoplay doesn't work after switching media
- FEC-4432 - [Android] Add support for offline playback in mobile
- FEC-4682 - Regression - dfp overly is shown on wrong place on Android 6.0
- OSMF-HLS plugin Buffers Refactor

* Mon Dec 21 2015 Jess Portnoy <jess.portnoy@kaltura.com> - v2.38.1-1
- TR-552 - CaaS widgets with playlist - On iOS thumbnail is out of alignment
- FEC-4565 - Send Notification in native bridge crashes
- FEC-4528 - drm playback : replay doesn't work , player stuck on spinning wheel
- FEC-4562 - Channel Playlist - chapters thumbnail doesn't change
- Fix mobile inlineScript loading

* Sat Dec 19 2015 Jess Portnoy <jess.portnoy@kaltura.com> - v2.38-1
- id3 tags support for Live HLS (native and flash)
- id3 tags support improved: time update interval has been reduced to 1 second
- New OSMF-HLS plugin 2.37 + id3 tags code
- FEC-4344 - webcast live event -cant move to old slide que point
- FEC-4433 - Add getLicenseData service in mwEmbed
- FEC-4035 - Support DASH stream with dash everywhere castlabs player
- PS-2381 - Doubleclick skipping two cue point midrolls ad, playing the Ad shows no video only audio
- FEC-4434 - Force playback engine flags don't enforce playable sources selection
- FEC-4427 - comScore Plugin Bugs
- FEC-3720 - Regression:External stream:plugin crushes and the stream is no longer playable
- FEC-3610 - VOD HLS: Player stuck on replay during throttling
- New OSMF-HLS plugin - massive buffers refactor
- FEC-4418 - Support flavorParamsId configuration option against download plugin
- FEC-4446 - silverlight player does not resolve playmanifest 302 redirect header http
- FEC-3832 - heartbeat: add config of heartbeat plugin to studio
- FEC-4431 - clipTo param is trimmed from manifest request when using Flash HDS
- SUP-6647 - alert-container text overflows
- SUP-6602 - no audio playback on Android
- SUP-6584 - Hovering controls subtitles issue
- SUP-6603 - Akamai Analytics: player uses default beacon URL instead of the one defined
- FEC-4389 - Enable player message to be overridden
- SUP-6535 - Change in Google Analytics plugin
- FEC-4462 - HLS OSMF - Seek in Kaltura DVR take more time than in previous player version
- FEC-4459 - HLS OSMF - take around 10-12 seconds to switch from DVR to Kaltura Live
- FEC-4458 - HLS OSMF - Kaltura Live with DVR loaded with 40-50 seconds of delay
- Fix IE8 variable-function name collision
- Fix PHP version syntax issues
- Add PiP plugin to support pip in iOS9
- FEC-4468 - Player layout is wrong in narrow bandwidth
- WB-2151 - Wrong spacing between buttons - OTT skin
- SUP-6143 - Player v2.35 - Icons Display
- FEC-4429 - (ClosedCaptions + playlist + hover-controls + IE8) != love
- FEC-4364 - Hard coded http fonts on some CSS files
- FEC-4125 - server side playback rate- rate selection doesn't work after changing media
- FEC-4472 - Regression : SDK - 2.0.5 Doesn't play any video with player version v2.38.rc9
- FEC-4481 - Regression: the players with autoEmbed type failed to be loaded
- FEC-4314 - if the number of items in the playlist is lower than MinClips, calculate mediaItemWidth according to it, else according to MinClips settings
- FEC-4068 - Display error on unsupported DRM use-cases
- FEC-3832 - trackEventMonitor function added to the studio config
- Fix PS modules not loading
- Fix DASH silverlight cross domain loading
- FEC-2648 - Rate Selector - Rate selector doesn't work in Chrome
- FEC-4503 - Player: While hovering over seek bar, the arrow pointer above it doesn't point to where user points
- FEC-4431 - clipTo param is trimmed from manifest request when using Flash HDS
- FEC-4500 - Channel Playlist - Playlist is not disabled during pre-roll Ad
- FEC-4484 - Improve Native Callout
- FEC-4521 - webcast with no DVR - after stop start of the video the player is freeze.
- FEC-4519 - Kaltura Live isn't starting to play after stop and re-run the stream
- FEC-4068 - DRM playback error handling
- FEC-4524 - Webcast NO DVR- player freeze for 10 sec when open
- Enable using MultiDRM with nativeCallout
- FEC-4533 - Hovering controls: After return from full screen mode, the "pause" button displayed forever on mobile devices
- FEC-4528 - drm playback : replay doesn't work , player stuck on spinning wheel
- Disable inlineScript in mobile devices
- FEC-4068 - Disable DASH on mobile Chrome, use on SDK
- FEC-4548 - start monitor on native onplay event instead of when clicking our play button
- FEC-4557 - Regression: Seek doesn't works for audio entry
- FEC-4554 #comment Reset chapters state on media change
- Fix DFP crash on empty player init
- updated comScoreStreamingTag plugin
- FEC-4554 - Channel Playlist - entry with chapters and slides not playable in channel playlist
- FEC-4561 - Channel playlist: impossible to change slides for audio LC if it part of playlist with Live stream
- KalturaHLS2 plugin removed

* Fri Dec 4 2015 Jess Portnoy <jess.portnoy@kaltura.com> - v2.37.3-1
- FEC-4446 - Fix issue with playback engine fail resolving URL redirect(HTTP 302)

* Sun Nov 22 2015 Jess Portnoy <jess.portnoy@kaltura.com> - v2.37.1-2
- Remove unneeded and yet very big modules/Widevine dir while packaging.

* Fri Nov 20 2015 Jess Portnoy <jess.portnoy@kaltura.com> - v2.37.1-1
- FEC-2823 - Google Analytics configuration in Studio is wrong
- FEC-3724 - uDRM: Modular DRM p2 is not working on IE11 & Edge
- FEC-3937 - Player Share is hardcoded to cdnapi.kaltura.com
- FEC-3982 - Related videos are stretched on fullscreen
- FEC-4063 - Share&Embed: white lines appear after click on some social network icon on FireFox
- FEC-4158 - Strings plugin should support per localization key overrides
- FEC-4236 - Add logic to the flavor selection in Android
- FEC-4253 - Captioning flyout does not disappear as expected
- FEC-4296 - Playlists should support setting playlist width in percentage
- FEC-4328 - Support hide cursor durring fullscreen playback
- FEC-4336 - evars and props do not get updated in playlist
- FEC-4349 - Fix native callout on Android
- FEC-4367 - moderation plugin: Thank you message not localized
- FEC-4394 - Seek race condition prevent seek events propagation in native player
- IVQ integration
- OPF-1572 - Issues with Sub-titles
- PLAT-3590 - Replace existing og:tags in KMC Preview & Embed links to support HTML5 playback on Facebook and Embedly
- Remove unneeded and yet very big modules/Widevine dir while packaging.
- SUP-5575 - Google analytics page display
- SUP-5910 - "EmbedPlayer.HidePosterOnStart" Attribute Overrides "EmbedPlayer.ShowPosterOnStop"
- SUP-5984 - URL Top syndicators
- SUP-5991 - "video content" tooltip is showing while the player loads
- SUP-6057 - Logo stretched on IE 9
- SUP-6097 - Changing playbackRate modifies number of captions
- SUP-6143 - Player v2.35 - Icons Display
- SUP-6313 - Live steam - the stream doesn't starts after the first click on the play button with embed type - thumbnail and embed
- SUP-6372 - Size of cookie request header field exceeds server limit.
- WEBC-581 - keyboard shortcuts are not disabled in in-player Q&A
- fix chromecast HLS support*
- SUP-5072 - YouTube player autoplay fails
- FEC-4417 - IMA issue - When preroll ended the media content ended the player can't replay
- FEC-4414 - Scrubber head is sometimes cut during playback in Chrome latest version
- FEC-4413 - multiple "doStop" notifications causes the video to load in iOS mobile devices
- SUP-6540 - Fallback from Flash to HTML5 v2.36 causes an endless wheel GUI issue
- FEC-3844 - Rate selector: the video started to play at beginning, if seek it and after increase speed
- SUP-6312 - mwe-embedplayer-no-source not respected

* Thu Oct 22 2015 Jess Portnoy <jess.portnoy@kaltura.com> - v2.36-1
- SUP-5808 - Watermark test page uses outdated attribute names
- SUP-5902 - Video Invisible For Contrast Function of Windows OS
- FEC-3786 - Captions- 'Set as default' button does not work
- FEC-4162 - Channel playlist - playlist button look disabled in live event that had not start
- SUP-5515 - VPAID Overlay positioning issue
- KMS-8968 - In Video Quizzes: Questions are not pop-upped in youtube entry
- KMS-8929 - Channel Playlist - when Live/Webcast Live event should start to play, all playlists entries displayed grey out
- FEC-4155 - regression : HLSMultiAudioFlashTest test page not working
- FEC-3938 - Start Over + Catchup + VOD test support
- FEC-4055 - Android not being able to play stream on Onprem solution, and works fine on SaaS
- SUP-5971 - [2.34 Regression] EmbedPlayer.EnableIpadHTMLControls=false no longer shows native controls
- FEC-4162 - Channel playlist - playlist button look disabled in live event that had not start
- FEC-4151 - v2.35 Error: Using non-prodcution version of kaltura player library.
- FEC-4179 - airPlay plugin doesn't work
- FEC-4080 - Kaltura Live with DVR through HLS failed to be load
- FEC-4200 - Channel playlist: No Vast pre-roll playing before LC entries on iPad
- FEC-4219 - Channel playlist: YouTube entry failed to be start on iPhone if previous entry also has been YouTube
- FEC-3127 - Playlist should support playlist scroll to current entry
- FEC-4255 - Audio starting no from beginning for specific customer's stream
- FEC-4219 - Channel playlist: YouTube entry failed to be start on iPhone if previous entry also has been YouTube
- FEC-4211 - Seek is not not released if performing seek to current position
- FEC-4185 - omniture: name of ad is not reported in the omniture events (vast)
- WEBC-627 - Support multiple presenters/moderators
- FEC-4258 - Google Analytics playr plug-in - setAlllowLinker attribute support
- FEC-3127 - Playlist should support playlist scroll to current entry
- FEC-3967 - scubber doesn't make any progress when playing the AES stream
- FEC-4297 - Playlist with DFP: after seek video, possible to select other entry during Ad that causes to unexpected behavior
- Enable suppressing non production URLs error message
- New Chromecast custom receiver app
- Youbora fixes
- Smart Client fixes
- New HLS plugin
- Correcting Impression and Tracking URL calling for multiple Vast Wrapper feeds.
- Channel playlist dual screen support
- Changed checking for Vast Element in ad XML to explicitely look for an element node.

* Thu Oct 8 2015 Jess Portnoy <jess.portnoy@kaltura.com> - v2.35.5-1
- IVQ release

* Thu Sep 17 2015 Jess Portnoy <jess.portnoy@kaltura.com> - v2.35-1
- FEC-4021 - Video is not playing on IOS9 while it has overly
- FEC-4012 - Seek on ios 9 : presents only sound on DFP midroll
- FEC-4010 - Main video on playlist slides down
- FEC-4030 - Switching between slides stack the video on spinner, on IOS-9
- FEC-4032 - Video is not replayed on : Vast pre-roll with interval (IOS-9)
- FEC-4031 - Seek is not working on IOS-9 - spinner is shown
- FEC-4026 - video can't be replayed on IOS-9 in API player
- FEC-4025 - PlaylistReady event is sent untimely (looped) on playlist on IOS-9
- FEC-4028 - Vast postroll playing twice - video does not play and keeps loading forever on IOS-9
- FEC-4029 - Video is not playing while has vast tracking on non-linear ad
- FEC-4016 - Playhead is not updated to progress time on IOS-9 after DFP midroll (audio entry)
- FEC-4011 - Fullscreen is not enlarged to the ios 9 screen entirely
- FEC-3814 - Share & Embed basic - User not able log in to any social media on Microsoft Edge
- FEC-4013 - While seek on IOS-9 in player with DFP pre-mid-postroll - Replay will not work
- FEC-4019 - VMAP_post_linear is not skipped
- FEC-4064 - YouTube playlist - can't change entry
- PLAT-3588 - Add playMainfest paramater for timealign removal of source flavor for wowza live streaming
- SUP-5515 - VPAID Overlay positioning issue
- FEC-4039 - Green marks on the video and video freezes on Firefox
- FEC-3720 - External stream: plugin crushes and the stream is no longer playable
- FEC-4040 - Video is not smooth and jumps
- FEC-4067 - Omniture is not sending additional evars and props to view events
- FEC-4069 - Support load with KS with slashes parameterization ( does not work ?ks param )
- SUP-5512 - Download link not working in versions 2.33
- FEC-4066 - The player don`t display the sync point and the Admin player plays HLS instead of HDS.
- FEC-2522 - Support DFP VAST VPAID engine: Kaltura cuePoints, API invocation and partial mediaProxy cuePoint override
- FEC-4087 - Re-evaluate mediaName before sending the 1st event
- FEC-2693 - Lecture Capture: the LC menu appears also for VOD entries, if LC and VOD included in playlist
- FEC-4088 - The mixed playlist with youtube entries doesn't work properly
- SUP-4784 - Entry duration presented with an additional second
- SUP-5206 - Player CC button - UI issue
- SUP-5184 - Player CC - UI issues
- SUP-5353 - emebed - Full Screen playback on IE9 fails due to domain restrictions
- SUP-5635 - Large button size in a custom style causes misalignment in "Share" screen
- FEC-3173 - Google Analytics: Support custom event category and custom labels
- FEC-4038 - Update Buffer documentation and add buffer duration to events and mediaProxy
- FEC-3905 - Support NPAW youbora analytics plugin
- FEC-4079 - Some entries play with interrupts
- FEC-4094 - In-Video Quizzes: YouTube entry: Playback time & scrubber synchronization issue
- SUP-5573 - Question - player events and logs
- FEC-4091 - Auto play and auto continue don't work for YouTube playlist
- FEC-4090 - spinner stuck on youtube entry after seek
- FEC-4074 - Tokenization for v2.34
- FEC-4096 - YouTube playlist: the playlist doesn't load if delivery type is Kaltura auto or HDS
- FEC-4095 - Source not found player error
- FEC-3820 - ad pod events are not sent to reporting server
- FEC-3559 - allow overriding the ServiceUrl and CdnUrl completely by passing respective flashvars
- FEC-3820 - ad pod events are not sent to reporting server
- SUP-5849 - Scrubber arrow location with aspect ratio
- KMS-8879 - Channel Playlist - Cannot handle upcoming Live/Webcast event
- FEC-4100 - YouTube playlist: need to tap twice on screen in order to pause YouTube entry on Android and iOS
- FEC-4099 - Youtube and KMC playlist: impossible to change playing entry from YouTube to KMC or vice versa on Android and iOS
- FEC-4098 - YouTube playlist disabled after player loads on Android or iOS devices
- FEC-4097 - YouTube playlist with auto play - the video doesn't start, black screen appears on Android and iOS devices
- FEC-4092 - YouTube playlist: black screen in player area appears after refreshing the test page
- FEC-4093 - Lecture Capture: the LC menu/controls appear also for Kaltura live entries in combined playlist
- FEC-3974 - "wrong reference id" message does not appear when using wrong reference id as source
- FEC-4131 - can't play live with ad stitching specific stream
- FEC-4122 - Lecture capture - Video plays in the main screen when stream is selected
- FEC-4120 - Multiple Playlists Monetization - Clicking an overlay ad pauses the video instead of open the target page
- New HLS-OSMF plugin
- Improved IE8 detection *

* Tue Sep 15 2015 Jess Portnoy <jess.portnoy@kaltura.com> - v2.34-3
- Create cache dir under web/html5/html5lib/$i/cache and set write perms for Apache
- Symlink LocalSettings.php to /opt/kaltura/app/configurations/html5.php
- kaltura-html5lib depends on kConf.php provided by kaltura-base so a Requires: kaltura-base is needed

* Thu Aug 20 2015 Jess Portnoy <jess.portnoy@kaltura.com> - v2.34-1
- SUP-5551 - Source selector doesn't work after changing media
- SUP-5535 - Large Play button - Bug in "Custom styles"
- SUP-5468 - Font color change in chapters
- SUP-5428 - Image player causes insecure content to load
- SUP-5398 - If flash disabled, player fallback to http progressive and displays auto only in source selector
- SUP-5397 - Scrubber is not released from the cursor after seeking
- SUP-5377 - Cannot change the time label font color
- SUP-5357 - Pause button stop working
- SUP-5356 - Disney - No playback when DoubleClick ad tag is null
- SUP-5262 - VAST Ads - Cause Endless Loop on iPhones 
- SUP-5260 - KMS - editing Clip not working properly
- SUP-5120 - Playback rate selector starts video from beginning when changing rate for first time
- SUP-4913 - Embed code does not play and the player's wheel keep spinning
- SUP-4911 - Postmedia - autoMute parameter is cached
- SUP-4721 - Play button disappears in 2.30 player in IE + iframe embed when in full screen

* Fri Jul 24 2015 Jess Portnoy <jess.portnoy@kaltura.com> - v2.33-1
- FEC-677 - volumeControl plugin should support verical layout
- FEC-3331 - Support server side playback Rate where not available client side or no progressive stream
- FEC-3678 - Make the entryList param dynamic for the related data 
- FEC-1755 - Adobe Analytics Omniture Heartbeat AppMeasurement player implmenation
- FEC-3509 - Design OTT Player Skin
- FEC-3733 - Anonymous user
- FEC-2900 - Implement embedly player.js interface for player API against kaltura player
- SUP-4886 - Disabling the Livstream redirect
- SUP-5119 - Playback rate selector issue
- SUP-4976 - changeMedia issue on Android 5.0
- SUP-5142 - VPAID Issues, clickthrough, portrait and playback
- SUP-4014 - Adtag link not working on HTML5 players
- SUP-4904 - Chapters names on menu not so visible on IE9
- SUP-5120 - Playback rate selector starts video from beginning when changing rate for first time
- SUP-5312 - Vast ads are not filling the player area
- SUP-4277 - Mediahuis - Windows Phone 8.1 black screen on playbac
- SUP-5278 - VPAID Overlay dimensions/position issue in full screen
- SUP-5357 - Pause button stop working
- SUP-5349 - Unable to change preferred bitrate in source selector

* Sun Jul 12 2015 Jess Portnoy <jess.portnoy@kaltura.com> - v2.32.1-1
- Support MSE/EME only on Chrome

* Sun Jun 28 2015 Jess Portnoy <jess.portnoy@kaltura.com> - v2.32-1
- FEC-3632 - Supprot all tremor ad substitutions
- FEC-3640 - Support large play button when DFP ads are paused.
- SUP-4897 - Download button leads to error
- SUP-4856 - SRT files with Mac line endings do not load
- SUP-4845 - YouTubePlayer should forceIframe by default
- SUP-4843 - Low quality in bumper ads
- SUP-4825 - SRT captions color change dynamically
- SUP-4277 - Mediahuis - Windows Phone 8.1 black screen on playback
- SUP-4182 - Firefox issue with right click menu
- SUP-4564 - Image while broadcasting live audio stream
- SUP-3568 - Change Iframe title from "Kaltura Embed Player iFrame" to the player's title
- SUP-4998 - Query - Defining one thumbnail URL for all entries while using thumbnail embed
- SUP-5070 - abChecker plugin not working
- SUP-4857 - Accessibility issue
- SUP-5051 - Universal Player probes for Java's runtime
- SUP-5002 - Captions issue with player version 2.31 in Desktop and Android
- SUP-3590 - Translating error message from English to Dutch


* Sun May 31 2015 Jess Portnoy <jess.portnoy@kaltura.com> - v2.31-1
- FEC-3185 - Add paging ability to core playlist
- FEC-3504 - Add playSessionId to each playmanifest
- FEC-3502 - Do not display slides, scubber or chapters when no DVR info is avalaible
- FEC-2412 - Support configuration on flavor selector to display bitrate instead of size
- SUP-4030 - Letterboxing bug when setting player for live stream
- SUP-4589 - GroovyGecko - Google Analytics urchinCode plugin
- SUP-4509 - Downloading a specific flavor
- SUP-4237 - Rate Selector - speed conversion not working properly 
- SUP-3568 - Change Iframe title from "Kaltura Embed Player iFrame" to the player's title
- SUP-4621 - Player Analytics regression around statistics properties
- SUP-3383 - "Install Flash" message not shown on IE8
- SUP-3590 - Translating error message from English to Dutch 
- SUP-4572 - issue with video on application for iOS devices
- SUP-4129 - Page zoomed in after exiting fullscreen
- SUP-4678 - Full screen issue in Android Galaxy Note and Galaxy S3

* Mon May 4 2015 Jess Portnoy <jess.portnoy@kaltura.com> - v2.30-1
- FEC-3100 - Support DFP player identification
- SUP-3177 - [v2.20] Player stuck when seeking on Firefox/OSX, webm flavor
- SUP-3404 - Youtube videos will not load if Audio Description Plugin Enabled
- SUP-3569 - Flicking TTML captions
- SUP-3648 - Pausing on iPhone jumps to 00:00:15
- SUP-3684 - Thumbnail at the end of a live stream
- SUP-3864 - Download gets cut for large flavors
- SUP-4003 - language of default captions will be chosen by browser language
- SUP-4077 - Video Player Voice Over Accessibility Issue
- SUP-4168 - [2.28] No progress or countdown indication for a DoubleClick ad
- SUP-4213 - Video quality drop with player version 2.28 - preferedFlavorBR not respected
- SUP-4250 - VAST preroll not respected in 2.28 on mobile.
- SUP-4277 - Mediahuis - Windows Phone 8.1 black screen on playback
- SUP-4473 - 2.29: "Stack overflow at line: 0" at end of playback on IE8
- SUP-4546 - Embed code for video with chaptering is not loading
- SUP-3314 - Player dimensions in Universal Studio 
- SUP-4232 - Black screen in IE when viewing videos in full screen
- SUP-4051 - Downloading from player yields 0 bytes files

* Sun Apr 5 2015 Jess Portnoy <jess.portnoy@kaltura.com> - v2.29-1
- SUP-3340 - Live stream freezes for a few seconds when streaming with KRecord
- SUP-4096 - [2.27.1] document.onclick is kept even after player is gone
- SUP-3793 - No video playing
- SUP-4018 - Thumbnail isn't Displayed in Audio Playlist
- SUP-3984 - [2.28-rc8] Previous captions <track> elements not removed from <video> upon changeMedia
- SUP-3944 - [2.27.1] EmbedPlayerYouTube fails with an exception
- SUP-4137 - v2.28 broken hotkey functionality (End Key)
- SUP-4119 - Handle hidden iframe player loading and display
- SUP-4198 - [BankOfAmericaSaaS] Captions request is being blocked
- SUP-3684 - Thumbnail at the end of a live stream
- SUP-4189 - Kaltura Player versions greater than 2.22 don't handle onTextData event data properly - Kaplan
- SUP-4118 - issues with SpotXchange integration
- SUP-3367 - V2 player fires 2~3 'doPlay' events when using the related videos
- SUP-3369 - Captions on live stream don't show (manual live streaming)
- SUP-3960 - Ad tag issue - KDP

* Sun Mar 8 2015 Jess Portnoy <jess.portnoy@kaltura.com> - v2.28-1
- FEC-417 - Player 2.0 - Share & Embed functionality
- FEC-2866 - Enable multi-stream for iPad viewers
- FEC-2918 - Add uiconf id to Google Analytics
- FEC-2620 - Support vast loadAdsOnPlay property
- SUP-3996 - Playlist player issus, BOA
- SUP-3967 - Player requests undefined ciu_szs param
- SUP-3649 - Adding Class to Spinner using Custom CSS | HTML5 Player
- SUP-3888 - [2.27.1] Captions cookie does not take any effect
- SUP-3830 - Player stuck on spinning in iOS after changeMedia is called
- SUP-3783 - Player and KMC not showing all the captions available
- SUP-3641 - playlist section vs. video section
- SUP-3849 - Downloading from player causes no extension on Firefox+Mac
- SUP-3858 - [2.26-2.27] Captions text color doesn't apply
- SUP-3850 - HDS source selector broken in 2.24-2.27
- SUP-3781 - Captions supported in KDP does not in HTML5
- SUP-3629 - Postmedia No playerPlayed event after prerolls and before contnet with DFP ads
- SUP-3340 - Live stream freezes for a few seconds when streaming with KRecord

* Sun Feb 8 2015 Jess Portnoy <jess.portnoy@kaltura.com> - v2.27-1
- SUP-3485 - Chapter playlist gaps and unresponsive in external URL (standalon page) | V2 player | Chapters plugin
- SUP-3559 - Player gives a "No source video was found"
- SUP-3616 - JS player API. changeMedia doesnt work
- SUP-3687 - HDS\HLS mediaPlayFrom\To does not work.
- SUP-3772 - preferred bitrate
- FEC-2055 - Playhead switch events are missing on all browsers (was: "Playhead switch events - Duration line has not been added under video on IE8") 
- FEC-2753 - Lecture capture Multiple stream: black screen instead of video when change stream on iPad
- FEC-2773 - Lecture capture : Chapters and switching streams - Timer & slide is wrong on iPad
- FEC-2809 - Related video does not work in FireFox on production

* Sun Jan 25 2015 Jess Portnoy <jess.portnoy@kaltura.com> - v2.26-1
- SUP-3609 - Misplaced playback on iPad with 2.24 & 2.25
- FEC-2611 - Chapters/Slides Menu (revised) - Playback

* Sun Jan 11 2015 Jess Portnoy <jess.portnoy@kaltura.com> - v2.25-1
- FEC-2611 - Chapters/Slides Menu (revised) - Playback
- FEC-1997 - lecture Capture - search , search results, no results.
- FEC-1971 - Support VPAID events mapping to VAST events
- SUP-3067 - Default captions malfunction 
- SUP-3396 - captions do not appear on v2 players
- SUP-3252 - doStop() function malfunction.
- SUP-3429 - Clipped duration not displayed on page load, but only after play 
- SUP-2937 - Thumbnail message in the beginning of entries
- SUP-3502 - HLS playback fails due to access control
- SUP-3496 - Change image file name when download with Universal studio
- SUP-3480 - Playlist player layout display issues in iOS/Android
- FEC-2594 - Playhead segment doesn't works - the video started to play from beginning
 
* Sun Jan 4 2015 Jess Portnoy <jess.portnoy@kaltura.com> - v2.24-2
- Neglected to include v2.21 v2.22 v2.23
- Use a for loop to iterate on vers.

* Sun Dec 28 2014 Jess Portnoy <jess.portnoy@kaltura.com> - v2.24-1
- FEC-1764 - Playback rate should support video tag interface switch.
- PS-1987 - PostMedia: Failed to block playback of domain restricted entries
- PS-1967 - (INTLKVP-133) Ads not played on Android stock browser
- PS-1912 - (INTLKVP-114) Ad completed event is not reported for post-roll on iPad Air (iOS 8)
- PS-1988 - PostMedia-iPad-iPhone-S4-nexus: Failed to load Geo Restricted playlist
- SUP-3377 - Universal player download button doesn't work right with image
- SUP-2991 - 508 v2 player - Audio description does not rewind
- SUP-2604 - Player don't load when "Rate Selector" is enabled | V2 player | customer site only
- SUP-3341 - [v2.22.1] changeMedia does not make player exit sharing
- SUP-3344 - Android 5.0 playback doesn't work | HTML 5 player
- SUP-3256 - [2.21] Fullscreen button does not lose focus; space exits fullscreen
- SUP-3290 - DFP Vast not working in IE9
- SUP-3393 - "changeMedia" notice failure to update segments or stream url

* Sun Dec 14 2014 Jess Portnoy <jess.portnoy@kaltura.com> - v2.23-1
- FEC-2316 - Support Akamai Media Analytics Logging for forceKPlayer flash mode
- FEC-2315 - Create Strings plugin demo page expand override to all keys
- FEC-2350 - DFP plugin should support pauseAdOnClick with default true
- FEC-2281 - VAST plugin should support pauseAdOnClick with default true
- SUP-28 - Design live UI buttons and user flow
- FEC-869 - Playhead should dynamically adjust per available DVR 
- FEC-1998 - Lecture Capture - select video stream
- SUP-3319 - Ad beacon don't fire the 100% track | V2 player
- SUP-3243 - Configure player logo to a non-clickable logo doesn't work on Firefox
- SUP-2985 - changeMedia notification from audio entry to video entry causes first-frame-freeze
- SUP-2604 - Player don't load when "Rate Selector" is enabled | V2 player | customer site only
- SUP-3322 - Playlist entries list is not responsive even tough video section is responsive.| Player V2

* Mon Dec 1 2014 Jess Portnoy <jess.portnoy@kaltura.com> - v2.22-1
- SUP-3001 - Pre-roll ads don't show and player freezes on iPad+iOS8+Safari (2.19.5)
- SUP-3078 - Source Selector display in bitrate instead of pixels when using HDS/Akamai/RTMP delivery
- SUP-2943 - Long titles wrap and distort elements on the top bar container
- SUP-3128 - Video thumbnail stretch in the iOS 8 web view and lose it aspect ratio.
- SUP-3132 - Control Bar Icons are not transparent
- SUP-3175 - Playlist disappears and full screen icon is incorrect when returning from fullscreen mode
- FEC-2150 - Buffer underrun should not cause "media not found" message

* Mon Nov 17 2014 Jess Portnoy <jess.portnoy@kaltura.com> - v2.21-1
- SUP-2939 - Request cookies are missing in header 
- SUP-2423 - Thumbnail in full screen looks bad due to resize
- SUP-2429 - V2 player, maximize/minimize full screen pause issue
- SUP-2808 - Set max # of clips for V2 playlist player via UIVar
- SUP-2926 - Video overlays ads when using "Share"
- SUP-3044 - Vast overlay ads issue

* Sun Nov 2 2014 Jess Portnoy <jess.portnoy@kaltura.com> - v2.20-1
- FEC-1012 - Player v2: Playlist component support
- FEC-1837 - Add disable mouse hover controls during ad playback controls
- SUP-2317 - Preferred downloaded flavor for download button doesn't persist from V1 to V2
- SUP-2549 - V2 player stuck when "adBlock" is enabled | VAST plugin
- SUP-2802 - Download specific flavor v2 player
- SUP-2833 - Enable initial playlist player poster and disable between videos
- SUP-3038 - autoMute flashvar doesn't always work
- SUP-2841 - V2 LiveRail Countdown Timer Non-Functiona
- SUP-2549 - V2 player stuck when "adBlock" is enabled | VAST plugin


* Sun Sep 21 2014 Jess Portnoy <jess.portnoy@kaltura.com> - v2.18.5-1
- ver bounce.

* Sun Aug 3 2014 Jess Portnoy <jess.portnoy@kaltura.com> - v2.15-1
- SUP-2413 - window.setInterval cause hTML5 player failure
- SUP-2459 - Multiple "Pause" events
- SUP-2499 - V2 with ad gets stuck before playing the video | Prod site | VAST | pre-roll
- SUP-2292 - 'Expand Player' icon overlaps with video content frame
- FEC-1611 - Video doesn't play when adblock is enabled (vast&Tremor&Doubleclick)
- FEC-1249 - KDP event mapping had mapping to non-existant html5 player events

* Thu Jul 10 2014 Jess Portnoy <jess.portnoy@kaltura.com> - v2.14-1
- SUP-2464 - Ellentube V2 Player Issue - Doubleclick plugin is not working when using chromeless
- SUP-2212 - playlist with restricted entries
- SUP-2291 - Thumbnail not displayed when clicking share
- SUP-2317 - Preferred downloaded flavor for download button doesn't persist from V1 to V2
- SUP-2323 - Playlist on V2 player
- SUP-2337 - black rectangle on share screen
- SUP-2381 - NielsenCombined plugin in HTML5 v2 player sends "ci=undefined" instead of clientId
- SUP-2386 - Send Notification "changeMedia" is not working in HTML5 player
- SUP-2427 - Ellentv.com V2 Player - "matchMedia is null" Error (Firefox)
- SUP-2431 - V2 player in iframe embed - close full screen is not working
- SUP-2440 - Player not sending playbackComplete when playback ends
- FEC-1394 - Error An error was experienced when playing the video on Chrome on fullscreen
- FEC-1517 - Need to add the option to navigate from related to a new window instead of switch-media
- FEC-1396 - needless fields in Widevine plugin
- FEC-1531 - imageDefaultDuration=2 is set by default in ui variables plugin 
- PS-988 - Browsers- Volume is always in full when page is refreshed. Doesn't remember last used volume level

* Sat Jun 14 2014 Jess Portnoy <jess.portnoy@kaltura.com> - v2.11-1
- SUP-2306 - Bumper Click URL Not Working
- SUP-2198 - Related plugin go into infinite loop
- SUP-1983 - HTML5 v2 - HTTPS embed will not load on HTTP page

* Thu May 22 2014 Jess Portnoy <jess.portnoy@kaltura.com> - v2.9-2
- Add repo URL to metadata.

* Wed May 21 2014 Jess Portnoy <jess.portnoy@kaltura.com> - v2.9-1
- SUP-2048 - Omniture tracking issue on mobile devices
- SUP-2108 - HTML5 V2 player - incorrect display in Share screen
- FEC-1371 - IE9:The alert of missing Widevine Video Optimizer plugin is twisted.
- FEC-1375 - Can't install widevine media optimizer on Firefox Mac.
- FEC-1373 - FF:When pressing on Widevine Video Optimizer plugin link error occurs.

* Thu Apr 24 2014 Jess Portnoy <jess.portnoy@kaltura.com> - v2.7-1
- SUP-1856 - [postmedia] sound turned off when next video plays after preroll
- SUP-1884 - changeMedia autoPlay issue
- SUP-1875 - Critical VAST bug for Postmedia
- SUP-1917 - SF 43560 - Postmedia - critical bug in FF
- SUP-1892 - Share URL of HTML5 player does not interpret "magic" substitution
- FEC-1125 - Omniture plugin should support Ad Events
- FEC-1172 - KDP API should remain active during ad playback
- FEC-1189 - PostMedia -- KM-38 : autoMute should not be used on "next" video
- FEC-1195 - Share fails in IE browsers in bad window.open call
- FEC-1196 - PostMedia: first image of video appearing after video is complete
- FEC-1197 - Share url text field is not evaluated in player v2
- FEC-1199 - [ postmedia ] IE9 Browser freezes with the attempt to replay the video
- FEC-1260 - Error on Firefox when changing media after vast pre-roll (with/without auto-play)
- FEC-1257 - ChangeMedia with autoplay does not hide large play button
- FEC-1219 - Custom share link cannot be copied from the link URL because it renders {mediaProxy.entry.id}

* Sun Apr 6 2014 Jess Portnoy <jess.portnoy@kaltura.com> - v2.6-1
- FEC-1029 - TAR - JAWS reading buttons twice
- FEC-1173 - "Replay" button needs to be pressed twice for staring to play
- FEC-1160 - merge api fix for related videos failure on identical requests

* Sun Mar 30 2014 Jess Portnoy <jess.portnoy@kaltura.com> - v2.5-6
- Copy the LocalSettings.php to all packaged HTML5 vers.

* Tue Mar 25 2014 Jess Portnoy <jess.portnoy@kaltura.com> - v2.5-1
- SUP-1608 - V2 player - Play From Start Time To End Time function not working 
- SUP-1426 - HTML5 v2.0.2 Error message displays when leaving webpage 
- SUP-1580 - Kaltura colored loading wheel showing up instead of custom (IE 8, 9, 10)
- SUP-1717 - share plugin - social networks configurations 
- SUP-1720 - V2 player - Loop uiVar get stuck

* Sun Mar 9 2014 Jess Portnoy <jess.portnoy@kaltura.com> - v2.4-1
- SUP-1393 - Player 2.1 with leadwithhtml5 does not work on a secure MediaSpace instance on Safari 
- SUP-1556 - HTML5 Player freezing when playing using Safari. 

* Sun Feb 23 2014 Jess Portnoy <jess.portnoy@kaltura.com> - v2.3-1
  Fixes:
  - Studio V2 support
  - supporting offline download kms app
  - SUP-1365 pass vpaid params to flash as vpaidAdParameter flashvar with encoded value
  - SUP-1461 captions does not work in IE8

* Sun Feb 9 2014 Jess Portnoy <jess.portnoy@kaltura.com> - v2.1.1-6
- Fixed https://github.com/kaltura/platform-install-packages/issues/24

* Tue Jan 28 2014 Jess Portnoy <jess.portnoy@kaltura.com> - v2.1.1-5
- LocalSettings.php is ALWAYS the same, it has no custom data, why not just bring it as part of the package??

* Wed Jan 15 2014 Jess Portnoy <jess.portnoy@kaltura.com> - v2.1.1-3
- Moved root dir to %{prefix}/web.

* Tue Jan 14 2014 Jess Portnoy <jess.portnoy@kaltura.com> - v2.1.1-2
- Added %%doc.

* Tue Jan 14 2014 Jess Portnoy <jess.portnoy@kaltura.com> - v2.1.1-1
- initial package.
