use std::str::from_utf8;

use integer_encoding::*;
use pyo3::prelude::*;

#[pyfunction]
pub fn xid(buf: &[u8], appid: &str, agent: &str) -> PyResult<String> {
    let mut i: usize = 1;
    let (appid_size, offset) = isize::decode_var(buf.get(i..).unwrap_or(&[]));
    i += offset;
    let app_id = if appid_size == -1 {
        appid
    } else {
        from_utf8(buf.get(i..(i + appid_size as usize)).unwrap_or(&[])).unwrap_or("")
    };
    i += if appid_size == -1 {
        0
    } else {
        appid_size as usize
    };
    let (timestamp, offset) = u64::decode_var(buf.get(i..).unwrap_or(&[]));
    i += offset;
    let (agent_size, offset) = isize::decode_var(buf.get(i..).unwrap_or(&[]));
    i += offset;
    let agent_id = if agent_size == -1 || agent_size == 0 {
        agent
    } else {
        from_utf8(buf.get(i..(i + agent_size as usize)).unwrap_or(&[])).unwrap_or(agent)
    };
    i += if agent_size == -1 {
        0
    } else {
        agent_size as usize
    };
    let (seq, _) = u64::decode_var(buf.get(i..).unwrap_or(&[]));

    let appid = app_id.to_string();
    Ok([
        appid.clone(),
        timestamp.to_string(),
        agent_id.to_string(),
        seq.to_string(),
    ]
    .join("^"))
}

/// A Python module implemented in Rust.
#[pymodule]
fn pinpoint_parser(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(xid, m)?)?;
    Ok(())
}
