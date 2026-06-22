Theme.json:
```json
{
  "theme_version": "1.0.8",
  "theme_framework_version": "0.6",

  "status_bars": {
    "default": "components/status_bars/status_bar.json",
    "network": "components/status_bars/status_bar_network.json",
    "recon": "components/status_bars/status_bar_recon.json",
    "min": "components/status_bars/status_bar_min.json",
    "gps" : "components/status_bars/status_bar_gps.json"
  },

  "generic_menus": {
    "tutorial": "components/tutorial.json",
    "os_licenses": "components/os_licenses.json",
    "management_ap_wizard": "components/management_ap_wizard.json",
    "client_mode_wizard": "components/client_mode_wizard.json",
    "evilwpa_wizard": "components/pineap/evilwpa_wizard.json",
    "power_menu": "components/dashboards/power_menu.json",
    "regulatory": "components/settings/regulatory.json",
    "dashboard_path": "components/dashboards/wargames_dashboard.json",
    "alerts_dashboard": "components/dashboards/dashboard_alerts.json",

    "pineap_pineap_submenu": "components/pineap/submenu_pineap_pineap.json",
    "pineap_evilwpa_submenu": "components/pineap/submenu_pineap_evilwpa.json",
    "pineap_filters_submenu": "components/pineap/submenu_pineap_filters.json",
    "pineap_openap_submenu": "components/pineap/submenu_pineap_openap.json",
    "pineap_ssidpool_submenu": "components/pineap/submenu_pineap_ssidpool.json",

    "settings_general_submenu": "components/settings/submenu_settings_general.json",
    "settings_display_submenu": "components/settings/submenu_settings_display.json",
    "settings_ringtone_submenu": "components/settings/submenu_settings_ringtone.json",
    "settings_network_submenu": "components/settings/submenu_settings_network.json",
    "settings_system_submenu": "components/settings/submenu_settings_system.json",
    "settings_datetime_submenu": "components/settings/submenu_settings_datetime.json",
    "settings_gps_submenu": "components/settings/submenu_settings_gps.json",
    "settings_updates_submenu": "components/settings/submenu_settings_updates.json",
    "settings_help_submenu": "components/settings/submenu_settings_help.json",
    "settings_about_submenu": "components/settings/submenu_settings_about.json",

    "recon_settings": "components/recon/recon_settings.json",
    "recon_band_settings": "components/recon/recon_band_settings.json",
    "recon_selected_ap_menu": "components/recon/recon_selected_ap_menu.json",
    "recon_selected_ap_client_menu": "components/recon/recon_selected_ap_client_menu.json",

    "pineap_menu": "components/dashboards/dashboard_pineap.json",
    "settings_menu": "components/dashboards/dashboard_settings.json"
  },

  "option_dialogs": {
    "option_dialog":  "components/dialogs/ui_option_dialog.json",
    "option_dialog_recon":  "components/dialogs/ui_option_dialog_recon.json",
    "option_dialog_alerts":  "components/dialogs/ui_option_dialog_alerts.json",
    "option_dialog_payloads":  "components/dialogs/ui_option_dialog_payloads.json",
    "option_dialog_narrow":  "components/dialogs/ui_option_dialog_narrow.json"
  },

  "duckyscript_list_picker": "components/dialogs/duckyscript_list_picker.json",

  "launch_payload_dialog_path": "components/dialogs/launch_payload_dialog.json",
  "payloads_dashboard_path": "components/dashboards/dashboard_payloads.json",
  "payloads_for_category_list_path": "components/payloads_for_category_list.json",
  "payload_log_path": "components/payload_log.json",

  "filter_list_path": "components/filter_list.json",
  "pineap_ssid_pool_list_path": "components/pineap_ssid_pool_list.json",
  "pineap_clients_list_path": "components/pineap/submenu_pineap_clients.json",

  "alerts_dialog_submenu_path": "components/alert_payloads_for_category_list.json",

  "low_battery_alert_path": "components/alerts/low_battery_alert.json",
  "critical_battery_alert_path": "components/alerts/critical_battery_alert.json",

  "error_dialog_path": "components/alerts/alert_error_dialog.json",
  "alert_dialog_path": "components/alerts/alert_info_dialog.json",
  "warning_dialog_path": "components/alerts/alert_warning_dialog.json",

  "spinner_path": "components/spinner.json",
  "boot_spinner_path": "components/boot_animation.json",

  "keyboard_path": "components/keyboards/ui_keyboard.json",
  "number_keyboard_path": "components/keyboards/ui_keyboard_numeric.json",
  "ip_keyboard_path": "components/keyboards/ui_keyboard_ip.json",
  "mac_keyboard_path": "components/keyboards/ui_keyboard_hex.json",

  "recon_payloads_dashboard_path": "components/dashboards/dashboard_recon_payloads.json",
  "recon_payloads_for_category_list_path": "components/recon_payloads_for_category_list.json",
  "recon_dashboard_path": "components/dashboards/dashboard_recon.json",
  "recon_lists": {
    "recon_list": "components/recon/recon_results_list.json"
  },
  "recon_ap_clients_list_path": "components/recon/recon_ap_clients_list.json",

  "edit_string_dialog_path": "components/dialogs/edit_string_dialog.json",
  "edit_ip_dialog_path": "components/dialogs/edit_ip_dialog.json",
  "edit_mac_dialog_path": "components/dialogs/edit_mac_dialog.json",
  "edit_number_dialog_path": "components/dialogs/edit_number_dialog.json",

  "confirmation_dialog_path": "components/dialogs/confirmation_dialog.json",

  "setup_wizard_path": "components/setup_wizard.json",
  "checking_for_updates_path": "components/check_for_updates.json",
  "developer_menu_path": "components/developer_menu.json",
  "lock_screen_path": "components/lock_screen.json",
  "buttons_locked_screen_path": "components/buttons_locked_screen.json",
  "device_too_hot_warning_path": "assets/warn_device_too_hot.png",
  "device_dimming_screen_path": "assets/warn_device_dimming_screen.png",
  "help_info_path": "assets/help_qr.png",
  "license_info_path": "assets/license_qr.png",
  "virtual_pager_info_path": "assets/virt_qr.png",

  "toggle_templates" : {
    "toggle": "components/templates/toggle.json",
    "green_toggle": "components/templates/green_toggle.json",
    "disabled_toggle": "components/templates/disabled_toggle.json",
    "checkbox": "components/templates/checkbox.json",
    "pineap_filter_mode": "components/templates/pineap_filter_mode.json",
    "disabled_pineap_filter_mode": "components/templates/disabled_pineap_filter_mode.json"
  },

  "string_templates": {
    "recon_payload_title": "components/templates/recon_payload_title.json",
    "recon_payload_title_selected": "components/templates/recon_payload_title_selected.json",
    "alert_payload_title": "components/templates/alert_payload_title.json",
    "alert_payload_title_selected": "components/templates/alert_payload_title_selected.json",
    "client_ssid": "components/templates/client_ssid.json",
    "client_ssid_selected": "components/templates/client_ssid_selected.json",
    "client_mac": "components/templates/client_mac.json",
    "client_mac_selected": "components/templates/client_mac_selected.json",
    "timestamp": "components/templates/timestamp.json",
    "spinner_text": "components/templates/spinner_text.json",
    "string": "components/templates/string.json",
    "payload_name": "components/templates/payload_name_in_list.json",
    "payload_name_selected": "components/templates/payload_name_in_list_selected.json",
    "alert_info_dialog_text": "components/templates/alert_info_dialog_text.json",
    "string_title": "components/templates/string_title.json",
    "selected_string": "components/templates/selected_string.json",
    "error_text": "components/templates/error_text.json",
    "confirmation_dialog_text": "components/templates/confirmation_dialog_text.json",
    "option_dialog_string": "components/templates/option_dialog_string.json",
    "option_dialog_string_selected": "components/templates/option_dialog_string_selected.json",
    "ssid_pool_string": "components/templates/ssid_pool_string.json",
    "ssid_pool_string_selected": "components/templates/ssid_pool_string_selected.json",
    "network_filter_string": "components/templates/network_filter_string.json",
    "network_filter_string_selected": "components/templates/network_filter_string_selected.json",
    "payload_title": "components/templates/payload_title.json",
    "list_count": "components/templates/list_count.json",
    "list_page_total": "components/templates/list_page_total.json",
    "list_page_current": "components/templates/list_page_total.json",
    "list_pagination_label": "components/templates/list_pagination_label.json"
  },

  "radio_templates": {
    "radio": "components/templates/radio.json",
    "selected_radio": "components/templates/selected_radio.json"
  },

  "signal_templates": {
    "signal": "components/templates/signal.json",
    "selected_signal": "components/templates/selected_signal.json"
  },

  "color_palette":{
    "black":{ "r":0, "g":0, "b":0 },
    "blue":{ "r":106, "g":210, "b":249 },
    "red":{ "r":250, "g":72, "b":9 },
    "dark_red":{ "r":110, "g":31, "b":23 },
    "yellow":{ "r":231, "g":197, "b":74 },
    "gray":{ "r":128, "g":128, "b":128 },
    "green":{ "r":42, "g":180, "b":42 },
    "dark_green":{ "r":2, "g":101, "b":2 },
    "disabled_light_gray":{ "r":167, "g":167, "b":167 },
    "disabled_dark_gray":{ "r":61, "g":61, "b":61 },
    "medium_gray":{ "r":100, "g":100, "b":100 },

    "orange":{ "r":214, "g":133, "b":39 },
    "dark_orange":{ "r":142, "g":76, "b":26 },
    "light_blue":{ "r":156, "g":226, "b":255 },
    "cyan":{ "r":96, "g":205, "b":205 },
    "dark_cyan":{ "r":40, "g":120, "b":120 },
    "purple":{ "r":132, "g":87, "b":162 },
    "dark_purple":{ "r":77, "g":45, "b":99 },
    "magenta":{ "r":205, "g":85, "b":155 },
    "dark_magenta":{ "r":120, "g":45, "b":90 },
    "light_green":{ "r":110, "g":220, "b":110 },
    "olive":{ "r":140, "g":135, "b":55 },
    "dark_olive":{ "r":80, "g":75, "b":30 },
    "brown":{ "r":120, "g":72, "b":30 },
    "tan":{ "r":200, "g":170, "b":120 },
    "teal":{ "r":48, "g":150, "b":140 },
    "dark_teal":{ "r":20, "g":90, "b":85 },
    "navy":{ "r":15, "g":35, "b":75 },
    "light_yellow":{ "r":250, "g":225, "b":120 },
    "soft_white":{ "r":230, "g":230, "b":220 }
  },

  "_unused" : {
    "commands" : {
      "restart_pineapd": "service pineapd restart",
      "restart_networking": "service network restart",
      "reboot": "reboot",
      "log_temps": "/root/battest.sh > /tmp/temps.log",
      "restart_go": "service pineapplepager restart"
    },

    "payload_shortcuts": {
      "test1": "/root/payloads/user/cat1/test1",
      "test2": "/root/payloads/user/cat1/test2"
    },

    "simple_images": {
    }
  }
}
```



Wargames structure:
```
wargames/
├── assets/
│   ├── alerts_dashboard/
│   │   ├── alerts_bg.png
│   │   └── sub.png
│   │   
│   ├── alert_dialog_bg_term.png
│   ├── alert_dialog_bg_term_blue.png
│   ├── alert_dialog_bg_term_error.png
│   ├── alert_dialog_bg_term_warning.png
│   ├── arrow_down.png
│   ├── arrow_up.png
│   ├── autoplay.png
│   ├── autoplay_stopped.png
│   ├── blank_recon_bg.png
│   ├── boot_animation/
│   │   ├── init-1.png
│   │   ├── init-2.png
│   │   ├── init-3.png
│   │   └── init-4.png
│   │   
│   ├── buttons_locked.png
│   ├── checkbox.png
│   ├── client.png
│   ├── confirmation_dialog/
│   │   ├── generic_confirmation_button_deselected.png
│   │   └── generic_confirmation_button_selected.png
│   │   
│   ├── confirmation_dialog_bg_term.png
│   ├── critical_battery_alert.png
│   ├── dashboard/
│   │   ├── alerts.png
│   │   ├── highlight.png
│   │   ├── item_bg.png
│   │   ├── payloads.png
│   │   ├── pineap.png
│   │   ├── recon.png
│   │   ├── settings.png
│   │   └── wargames_bg.png
│   │   
│   ├── dialog_bg.png
│   ├── disabled_client.png
│   ├── disabled_info.png
│   ├── disabled_keyboard.png
│   ├── disabled_warning.png
│   ├── disabled_wizard.png
│   ├── divider.png
│   ├── divleft.png
│   ├── divright.png
│   ├── down.png
│   ├── edit_string_dialog_bg.png
│   ├── flame.png
│   ├── folder.png
│   ├── help_qr.png
│   ├── info.png
│   ├── keyboard/
│   │   ├── keyboard_layout_hex.png
│   │   ├── keyboard_layout_ip.png
│   │   ├── keyboard_layout_lower.png
│   │   ├── keyboard_layout_numeric.png
│   │   ├── keyboard_layout_symbols.png
│   │   ├── keyboard_layout_upper.png
│   │   ├── _hex-bg.png
│   │   ├── _key-bg.png
│   │   └── _spacebar-4x.png
│   │   
│   ├── keyboard.png
│   ├── launch_payload_dialog/
│   │   ├── animation/
│   │   │   ├── anim_frame_1.png
│   │   │   └── anim_frame_2.png
│   │   │   
│   │   └── launch_payload_bg.png
│   │   
│   ├── license_qr.png
│   ├── lock_screen.png
│   ├── low_battery_alert.png
│   ├── menu.png
│   ├── menu_disabled.png
│   ├── messagebox.png
│   ├── optiondialog/
│   │   ├── button_bg.png
│   │   ├── button_outline.png
│   │   ├── check.png
│   │   ├── option_dialog_bg_narrow.png
│   │   ├── option_dialog_bg_windowed.png
│   │   ├── option_dialog_bg_windowed_green.png
│   │   ├── option_dialog_bg_windowed_purple.png
│   │   ├── option_dialog_bg_windowed_red.png
│   │   └── x.png
│   │   
│   ├── pager-16bit.png
│   ├── payloadlog/
│   │   ├── payload_complete_indicator.png
│   │   ├── payload_error_indicator.png
│   │   ├── payload_log_bg.png
│   │   ├── payload_running_indicator.png
│   │   ├── payload_stopped_indicator.png
│   │   ├── scroll_down_indicator.png
│   │   ├── scroll_pause_indicator.png
│   │   └── scroll_up_indicator.png
│   │   
│   ├── payloads_dashboard/
│   │   ├── arrow.png
│   │   ├── payloads_bg.png
│   │   └── recon_payloads_bg.png
│   │   
│   ├── payload_dialog_option_bg.png
│   ├── payload_dialog_selected_box.png
│   ├── payload_log_bg.png
│   ├── pineap_bg.png
│   ├── power_menu_bg.png
│   ├── radio/
│   │   ├── radio_border.png
│   │   └── radio_selected.png
│   │   
│   ├── recon/
│   │   ├── clients.png
│   │   ├── enc_open.png
│   │   ├── enc_wep.png
│   │   ├── enc_wpa2.png
│   │   ├── enc_wpa3.png
│   │   ├── recon_dashboard.png
│   │   ├── recon_list_bg.png
│   │   ├── rssi_0.png
│   │   ├── rssi_1.png
│   │   ├── rssi_2.png
│   │   └── rssi_3.png
│   │   
│   ├── settings_bg.png
│   ├── spinner/
│   │   ├── spinner1.png
│   │   ├── spinner2.png
│   │   ├── spinner3.png
│   │   └── spinner4.png
│   │   
│   ├── start.png
│   ├── statusbar/
│   │   ├── bluetooth.png
│   │   ├── dashboard_battery_charge_100.png
│   │   ├── dashboard_battery_charge_25.png
│   │   ├── dashboard_battery_charge_50.png
│   │   ├── dashboard_battery_charge_75.png
│   │   ├── dashboard_battery_full.png
│   │   ├── dashboard_battery_text.png
│   │   ├── dashboard_brightness_2.png
│   │   ├── dashboard_brightness_3.png
│   │   ├── dashboard_brightness_5.png
│   │   ├── dashboard_brightness_7.png
│   │   ├── dashboard_brightness_8.png
│   │   ├── database.png
│   │   ├── ghz_2.png
│   │   ├── ghz_25.png
│   │   ├── ghz_256.png
│   │   ├── ghz_26.png
│   │   ├── ghz_5.png
│   │   ├── ghz_56.png
│   │   ├── ghz_6.png
│   │   ├── ghz_off.png
│   │   ├── gps.png
│   │   ├── mute.png
│   │   ├── pcap.png
│   │   ├── vibrate.png
│   │   ├── volume_high.png
│   │   ├── volume_low.png
│   │   ├── volume_medium.png
│   │   └── wigle.png
│   │   
│   ├── swap.png
│   ├── toggle/
│   │   ├── disabled/
│   │   │   ├── circle.png
│   │   │   └── toggle_disabled_bg.png
│   │   │   
│   │   └── enabled
│   │   
│   ├── triangle.png
│   ├── up.png
│   ├── upgrade/
│   │   ├── checking_for_update-min.png
│   │   ├── downloading_upgrade.png
│   │   └── validating_upgrade.png
│   │   
│   ├── virt_qr.png
│   ├── warning.png
│   ├── warn_device_dimming_screen.png
│   ├── warn_device_too_hot.png
│   ├── wifi_icon.png
│   ├── wizard.png
│   └── x.png
│   
├── color_palette_preview.html
├── components/
│   ├── alerts/
│   │   ├── alert_error_dialog.json
│   │   ├── alert_info_dialog.json
│   │   ├── alert_warning_dialog.json
│   │   ├── critical_battery_alert.json
│   │   └── low_battery_alert.json
│   │   
│   ├── alert_payloads_for_category_list.json
│   ├── boot_animation.json
│   ├── buttons_locked_screen.json
│   ├── check_for_updates.json
│   ├── client_mode_wizard.json
│   ├── dashboards/
│   │   ├── dashboard_alerts.json
│   │   ├── dashboard_payloads.json
│   │   ├── dashboard_pineap.json
│   │   ├── dashboard_recon.json
│   │   ├── dashboard_recon_payloads.json
│   │   ├── dashboard_settings.json
│   │   ├── power_menu.json
│   │   └── wargames_dashboard.json
│   │   
│   ├── developer_menu.json
│   ├── dialogs/
│   │   ├── confirmation_dialog.json
│   │   ├── duckyscript_list_picker.json
│   │   ├── edit_ip_dialog.json
│   │   ├── edit_mac_dialog.json
│   │   ├── edit_number_dialog.json
│   │   ├── edit_string_dialog.json
│   │   ├── launch_payload_dialog.json
│   │   ├── ui_option_dialog.json
│   │   ├── ui_option_dialog_alerts.json
│   │   ├── ui_option_dialog_narrow.json
│   │   ├── ui_option_dialog_payloads.json
│   │   └── ui_option_dialog_recon.json
│   │   
│   ├── filter_list.json
│   ├── keyboards/
│   │   ├── ui_keyboard.json
│   │   ├── ui_keyboard_hex.json
│   │   ├── ui_keyboard_ip.json
│   │   └── ui_keyboard_numeric.json
│   │   
│   ├── lock_screen.json
│   ├── management_ap_wizard.json
│   ├── os_licenses.json
│   ├── payloads_for_category_list.json
│   ├── payload_log.json
│   ├── pineap/
│   │   ├── evilwpa_wizard.json
│   │   ├── submenu_pineap_clients.json
│   │   ├── submenu_pineap_evilwpa.json
│   │   ├── submenu_pineap_filters.json
│   │   ├── submenu_pineap_openap.json
│   │   ├── submenu_pineap_pineap.json
│   │   └── submenu_pineap_ssidpool.json
│   │   
│   ├── pineap_ssid_pool_list.json
│   ├── recon/
│   │   ├── recon_ap_clients_list.json
│   │   ├── recon_band_settings.json
│   │   ├── recon_results_list.json
│   │   ├── recon_selected_ap_client_menu.json
│   │   ├── recon_selected_ap_menu.json
│   │   └── recon_settings.json
│   │   
│   ├── recon_payloads_for_category_list.json
│   ├── settings/
│   │   ├── regulatory.json
│   │   ├── submenu_settings_about.json
│   │   ├── submenu_settings_datetime.json
│   │   ├── submenu_settings_display.json
│   │   ├── submenu_settings_general.json
│   │   ├── submenu_settings_gps.json
│   │   ├── submenu_settings_help.json
│   │   ├── submenu_settings_network.json
│   │   ├── submenu_settings_ringtone.json
│   │   ├── submenu_settings_system.json
│   │   └── submenu_settings_updates.json
│   │   
│   ├── setup_wizard.json
│   ├── spinner.json
│   ├── status_bars/
│   │   ├── status_bar.json
│   │   ├── status_bar_gps.json
│   │   ├── status_bar_min.json
│   │   ├── status_bar_network.json
│   │   └── status_bar_recon.json
│   │   
│   ├── templates/
│   │   ├── alert_info_dialog_text.json
│   │   ├── alert_payload_title.json
│   │   ├── alert_payload_title_selected.json
│   │   ├── checkbox.json
│   │   ├── client_mac.json
│   │   ├── client_mac_selected.json
│   │   ├── client_ssid.json
│   │   ├── client_ssid_selected.json
│   │   ├── confirmation_dialog_text.json
│   │   ├── disabled_pineap_filter_mode.json
│   │   ├── disabled_toggle.json
│   │   ├── error_text.json
│   │   ├── green_toggle.json
│   │   ├── list_count.json
│   │   ├── list_page_current.json
│   │   ├── list_page_total.json
│   │   ├── list_pagination_label.json
│   │   ├── network_filter_string.json
│   │   ├── network_filter_string_selected.json
│   │   ├── option_dialog_string.json
│   │   ├── option_dialog_string_selected.json
│   │   ├── payload_name_in_list.json
│   │   ├── payload_name_in_list_selected.json
│   │   ├── payload_title.json
│   │   ├── pineap_filter_mode.json
│   │   ├── radio.json
│   │   ├── recon_payload_title.json
│   │   ├── recon_payload_title_selected.json
│   │   ├── selected_radio.json
│   │   ├── selected_signal.json
│   │   ├── selected_string.json
│   │   ├── signal.json
│   │   ├── spinner_text.json
│   │   ├── ssid_pool_string.json
│   │   ├── ssid_pool_string_selected.json
│   │   ├── string.json
│   │   ├── string_title.json
│   │   ├── timestamp.json
│   │   └── toggle.json
│   │   
│   └── tutorial.json
│   
├── README
└── theme.json
```

