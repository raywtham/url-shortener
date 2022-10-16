import './App.css';
import { useState } from 'react';
import Container from '@mui/material/Container';
import Grid from '@mui/material/Grid';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Stack from '@mui/material/Stack';
import ContentCopyIcon from '@mui/icons-material/ContentCopy';
import axios from 'axios';

function App() {
  // set state
  const [urlInput, setUrlInput] = useState("");
  const [shortLink, setShortLink] = useState("");
  const [urlError, setUrlError] = useState("");

  // api call to get shortened link
  const submitData = async () => {
    try {
      const response = await axios({
        method: 'post',
        url: 'http://localhost:8000/shortenedurls/',
        data: {
          "long_url": urlInput,
        }
      });
      setShortLink(response.data.short_url);
    } catch (e) {
      setUrlError(e.response.data.long_url[0] || "Error calling API");
    }
  };

  const copyLink = () => {

    navigator.clipboard
      .writeText(shortLink)
      .then(() => {
        alert("successfully copied");
      })
      .catch(() => {
        alert("something went wrong");
      });
  }

  return (
    <div className="App">
      <Container style={{ height: "100vh" }}>
        <Grid container align="center" justify="center" alignItems="center" style={{ height: "95vh" }}>
          <Grid item xs={2} />
          <Grid item container xs={8} direction="column" display="flex" alignItems="center" >
            <h1>URL Shortener</h1>
            <Stack spacing={4} direction="column" alignItems="center">

              <TextField
                fullWidth
                size="small"
                id="urlEntry"
                placeholder="https://www.example.com"
                // label="URL to shorten"
                variant="outlined"
                // helperText="url"
                value={urlInput}
                onChange={(e) => {
                  setUrlInput(e.target.value);
                }}
              />
              {urlError}
              <Button
                color="success"
                variant="contained"
                onClick={() => {
                  submitData();
                }}
              >shorten</Button>

              <TextField
                id="shortLink"
                fullWidth
                size="small"
                value={shortLink}
                variant="filled"
                // defaultValue=""
                sx={{ input: { color: 'white' }}}
                InputProps={{
                  readOnly: true,
                }}
              />

              <Button startIcon={<ContentCopyIcon />}
                variant="contained"
                onClick={() => {
                  copyLink(); 
                }}>copy</Button>
            </Stack>
          </Grid>
        </Grid>
      </Container>
    </div>

  );
}

export default App;
