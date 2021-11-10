import 'dart:io';
import 'package:attend/qrcamera.dart';
import 'package:attend/settings.dart';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:device_info_plus/device_info_plus.dart';

void main() => runApp(MaterialApp(
      title: "App",
      home: Home(),
    ));

class Home extends StatefulWidget {
  @override
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<Home> {
  int _currentPage = 0;
  Future<String> getdeviceId() async {
    var deviceInfo = DeviceInfoPlugin();
    if (Platform.isIOS) {
      var iosDeviceInfo = await deviceInfo.iosInfo;
      return iosDeviceInfo.identifierForVendor; // unique ID on iOS
    } else {
      var androidDeviceInfo = await deviceInfo.androidInfo;
      return androidDeviceInfo.androidId; // unique ID on Android
    }
  }

  Widget build(BuildContext context) {
    return MaterialApp(
      routes: {"/qr": (context) => QRCamera()},
      title: 'Flutter Demo',
      theme: ThemeData(primarySwatch: Colors.blue, brightness: Brightness.dark),
      home: SafeArea(
        child: Scaffold(
          floatingActionButton: FloatingActionButton(
              onPressed: () async {
                print("work");
                String deviceId = await getdeviceId();
                print(deviceId);
                Navigator.of(context)
                    .push(MaterialPageRoute(builder: (context) => QRCamera()));
              },
              child: Icon(Icons.camera_alt_rounded)),
          bottomNavigationBar: BottomNavigationBar(
            type: BottomNavigationBarType.fixed,
            backgroundColor: Color(0xffFF1FA5),
            currentIndex: _currentPage,
            selectedItemColor: Colors.white,
            unselectedItemColor: Colors.white.withOpacity(.60),
            selectedFontSize: 14,
            unselectedFontSize: 14,
            onTap: (value) {
              setState(() {
                _currentPage = value;
              });
            },
            items: [
              BottomNavigationBarItem(
                label: "Dashboard",
                icon: Icon(Icons.dashboard_rounded),
              ),
              BottomNavigationBarItem(
                label: "Settings",
                icon: Icon(Icons.settings),
              ),
            ],
          ),
          appBar: AppBar(
            title: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Text(
                  "Attend",
                  style: GoogleFonts.prompt(fontSize: 26),
                )
              ],
            ),
          ),
          body: IndexedStack(index: _currentPage, children: [
            Dashboard(),
            Settings(),
          ]),
        ),
      ),
    );
  }
}

class Dashboard extends StatelessWidget {
  const Dashboard({
    Key key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(20.0),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            "Welcome,",
            style: GoogleFonts.prompt(
                fontSize: 24, color: Colors.white.withOpacity(0.5)),
          ),
          Text(
            "Yajat Vishwakarma",
            style:
                GoogleFonts.prompt(fontSize: 48, fontWeight: FontWeight.bold),
          ),
          SizedBox(
            height: 50,
          ),
          Card(
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(15.0),
            ),
            child: Padding(
              padding: const EdgeInsets.all(20.0),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Text("Last Scanned",
                          style: GoogleFonts.prompt(
                              fontSize: 18,
                              color: Colors.white.withOpacity(0.5))),
                      Text("30/69", style: GoogleFonts.prompt(fontSize: 18)),
                    ],
                  ),
                  Text(
                    "Math's Class",
                    style: GoogleFonts.prompt(
                        fontSize: 36, fontWeight: FontWeight.w400),
                  ),
                  Row(
                    children: [
                      Padding(
                        padding: const EdgeInsets.only(right: 8),
                        child: Text(
                          "teacher",
                          style: GoogleFonts.prompt(fontSize: 18),
                        ),
                      ),
                      Container(
                        width: 5,
                        height: 5,
                        decoration: BoxDecoration(
                          shape: BoxShape.circle,
                          color: Colors.deepPurpleAccent,
                        ),
                      ),
                      Padding(
                        padding: const EdgeInsets.all(8.0),
                        child: Text(
                          "teacher",
                          style: GoogleFonts.prompt(fontSize: 18),
                        ),
                      ),
                      Container(
                        width: 5,
                        height: 5,
                        decoration: BoxDecoration(
                          shape: BoxShape.circle,
                          color: Colors.deepPurpleAccent,
                        ),
                      ),
                      Padding(
                        padding: const EdgeInsets.all(8.0),
                        child: Text(
                          "teacher",
                          style: GoogleFonts.prompt(fontSize: 18),
                        ),
                      ),
                    ],
                  )
                ],
              ),
            ),
          )
        ],
      ),
    );
  }
}
