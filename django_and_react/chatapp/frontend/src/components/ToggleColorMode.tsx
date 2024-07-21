import { useMediaQuery } from "@mui/material";
import { ReactNode, useCallback, useEffect, useMemo, useState } from "react";

interface Props {
  children: ReactNode;
}

const ToggleColorMode = ({ children }: Props) => {
  const [mode, setMode] =
    // useState<"light" | "dark">(() => localStorage.getItem("colorMode") as "light" | "dark") || (useMediaQuery("([prefers-color-scheme:dark") ? "dark" : "light");
    // useState<"light" | "dark">(() => localStorage.getItem("colorMode")?localStorage.getItem("colorMode") as "light" | "dark" :"light"  )
    useState<string>(() =>
      localStorage.getItem("colorMode")
        ? (localStorage.getItem("colorMode") as string )
        : "light"
    );

  const toggleColorMode = useCallback(() => {
    setMode((prevMode) => (prevMode === "light" ? "dark" : "light"));
  }, []);

  useEffect(()=>{localStorage.setItem("colorMode",mode)},[mode])
  const colorMode=useMemo(()=>({toggleColorMode}),[toggleColorMode])
  
};
export default ToggleColorMode