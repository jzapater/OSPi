#!/usr/bin/python

class gv:
    """An empty class for storing global vars."""
    pass

options = ([
    [_("System name"),"string","name", _("Unique name of this OpenSprinkler system."), _("System")],
    [_("Location"),"string","loc", _("City name or zip code. Use comma or + in place of space."),_("System")],
    [_("Language"),"list","lang", _("Select language (effective after reboot.)"),_("System")],
    [_("Time zone"),"int","tz", _("Example: GMT-4:00, GMT+5:30 (effective after reboot.)"),_("System")],
    [_("24-hour clock"),"boolean","tf", _("Display times in 24 hour format (as opposed to AM/PM style.)"),_("System")],
    [_("HTTP port"),"int","htp", _("HTTP port (effective after reboot.)"),_("System")],
    [_("Disable security"),"boolean","ipas", _("Allow anonymous users to access the system without a password."),_("Change Password")],
    [_("Current password"),"password","opw", _("Re-enter the current password."),_("Change Password")],
    [_("New password"),"password","npw", _("Enter a new password."),_("Change Password")],
    [_("Confirm password"),"password","cpw", _("Confirm the new password."),_("Change Password")],
    [_("Sequential"),"boolean","seq", _("Sequential or concurrent running mode."),_("Station Handling")],
    [_("Extension boards"),"int","nbrd", _("Number of extension boards."),_("Station Handling")],
    [_("Station delay"),"int","sdt", _("Station delay time (in seconds), between 0 and 240."),_("Station Handling")],
    [_("Master station"),"int","mas", _("Select master station."),_("Configure Master")],
    [_("Master on adjust"),"int","mton", _("Master on delay (in seconds), between +0 and +60."),_("Configure Master")],
    [_("Master off adjust"),"int","mtoff", _("Master off delay (in seconds), between -60 and +60."),_("Configure Master")],
    [_("Use rain sensor"),"boolean","urs", _("Use rain sensor."),_("Rain Sensor")],
    [_("Normally open"),"boolean","rst", _("Rain sensor type."),_("Rain Sensor")],
    [_("Enable logging"),"boolean","lg", _("Log all events - note that repetitive writing to an SD card can shorten its lifespan."),_("Logging")],
    [_("Max log entries"),"int","lr", _("Length of log to keep, 0=no limits."),_("Logging")]
])