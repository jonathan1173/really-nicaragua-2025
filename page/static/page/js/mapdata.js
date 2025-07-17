var simplemaps_countrymap_mapdata = {
  main_settings: {
    //General settings
    width: "responsive", //'700' or 'responsive'
    background_color: "#87CEEB", // Celeste cielo (SkyBlue)
    background_transparent: "no",
    border_color: "#fff",

    //State defaults
    state_description: "",
    state_color: "#88A4BC",
    state_hover_color: "#3B729F",
    state_url: "",
    border_size: 1.5,
    all_states_inactive: "no",
    all_states_zoomable: "yes",

    //Location defaults
    location_description: "Location description",
    location_url: "",
    location_color: "#FF0067",
    location_opacity: 0.8,
    location_hover_opacity: 1,
    location_size: 25,
    location_type: "square",
    location_image_source: "frog.png",
    location_border_color: "#FFFFFF",
    location_border: 2,
    location_hover_border: 2.5,
    all_locations_inactive: "no",
    all_locations_hidden: "no",

    //Label defaults
    label_color: "#ffffff",
    label_hover_color: "#ffffff",
    label_size: 16,
    label_font: "Arial",
    label_display: "auto",
    label_scale: "yes",
    hide_labels: "no",
    hide_eastern_labels: "no",

    //Zoom settings
    zoom: "yes",
    manual_zoom: "yes",
    back_image: "no",
    initial_back: "no",
    initial_zoom: "-1",
    initial_zoom_solo: "no",
    region_opacity: 1,
    region_hover_opacity: 0.6,
    zoom_out_incrementally: "yes",
    zoom_percentage: 0.99,
    zoom_time: 0.5,

    //Popup settings
    popup_color: "white",
    popup_opacity: 0.9,
    popup_shadow: 1,
    popup_corners: 5,
    popup_font: "12px/1.5 Verdana, Arial, Helvetica, sans-serif",
    popup_nocss: "no",

    //Advanced settings
    div: "map",
    auto_load: "no",
    url_new_tab: "no",
    images_directory: "default",
    fade_time: 0.1,
    link_text: "View Website",
    popups: "detect",
    state_image_url: "",
    state_image_position: "",
    location_image_url: ""
  },
  state_specific: {
    NIAN: {
      name: "Atlántico-Norte",
    },
    NIAS: {
      name: "Atlántico-Sur"
    },
    NIBO: {
      name: "Boaco"
    },
    NICA: {
      name: "Carazo"
    },
    NICI: {
      name: "Chinandega"
    },
    NICO: {
      name: "Chontales"
    },
    NIES: {
      name: "Estelí"
    },
    NIGR: {
      name: "Granada"
    },
    NIJI: {
      name: "Jinotega"
    },
    NILE: {
      name: "León"
    },
    NIMD: {
      name: "Madriz"
    },
    NIMN: {
      name: "Managua"
    },
    NIMS: {
      name: "Masaya",
      url: ""
    },
    NIMT: {
      name: "Matagalpa"
    },
    NINS: {
      name: "Nueva-Segovia"
    },
    NIRI: {
      name: "Rivas"
    },
    NISJ: {
      name: "Rio-San-Juan"
    }
  },
  locations: {},
  labels: {
    NIAN: {
      name: "Atlántico Norte",
      parent_id: "NIAN"
    },
    NIAS: {
      name: "Atlántico Sur",
      parent_id: "NIAS"
    },
    NIBO: {
      name: "Boaco",
      parent_id: "NIBO"
    },
    NICA: {
      name: "Carazo",
      parent_id: "NICA"
    },
    NICI: {
      name: "Chinandega",
      parent_id: "NICI"
    },
    NICO: {
      name: "Chontales",
      parent_id: "NICO"
    },
    NIES: {
      name: "Estelí",
      parent_id: "NIES"
    },
    NIGR: {
      name: "Granada",
      parent_id: "NIGR"
    },
    NIJI: {
      name: "Jinotega",
      parent_id: "NIJI"
    },
    NILE: {
      name: "León",
      parent_id: "NILE"
    },
    NIMD: {
      name: "Madriz",
      parent_id: "NIMD"
    },
    NIMN: {
      name: "Managua",
      parent_id: "NIMN"
    },
    NIMS: {
      name: "Masaya",
      parent_id: "NIMS"
    },
    NIMT: {
      name: "Matagalpa",
      parent_id: "NIMT"
    },
    NINS: {
      name: "Nueva Segovia",
      parent_id: "NINS"
    },
    NIRI: {
      name: "Rivas",
      parent_id: "NIRI"
    },
    NISJ: {
      name: "Rio San Juan",
      parent_id: "NISJ"
    }
  },
  legend: {
    entries: []
  },
  regions: {},

};

