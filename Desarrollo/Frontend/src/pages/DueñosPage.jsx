import React from "react";
import EditarDueño from "../components/dueños/EditarDueño";
import RegistrarDueño from "../components/dueños/RegistrarDueño";
import ListarDueños from "../components/dueños/ListarDueño";
import { Typography } from "@mui/material";
import BottomBar from "../components/BottomBar";
import Navbar from "../components/NavBar";

function DueñosPage() {
    return (
        <div>
            <Navbar />
            <Typography variant="h1">Dueños</Typography>
            <BottomBar />
            <RegistrarDueño />
            <EditarDueño />
            <ListarDueños />
        </div>
    );
}

export default DueñosPage;