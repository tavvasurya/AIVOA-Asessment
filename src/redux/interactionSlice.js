import { createSlice } from "@reduxjs/toolkit";

const interactionSlice = createSlice({
  name: "interaction",
  initialState: {
    response: null,
  },
  reducers: {
    setResponse: (state, action) => {
      state.response = action.payload;
    },
  },
});

export const { setResponse } = interactionSlice.actions;
export default interactionSlice.reducer;
