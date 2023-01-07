import React from "react";
import { createRoot } from "react-dom/client";
import {createBrowserRouter, RouterProvider} from "react-router-dom";
import 'bootstrap/dist/css/bootstrap.css';

import Home from "./pages/Home";
import Styles from "./assets/css/main.css"

const router = createBrowserRouter([
  {
    path: "/",
    element: <Home></Home>,
  },
  {
    path: "about",
    element: <Home></Home>,
  },
]);

createRoot(document.getElementById("root")).render(
  <RouterProvider router={router} style={Styles}/>
);
