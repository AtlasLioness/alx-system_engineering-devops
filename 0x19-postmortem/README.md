# Postmortem: Website Outage on July 15, 2024

## Issue Summary

**Duration**: The outage lasted for 2 hours, from 08:00 AM to 10:00 AM UTC.  
**Impact**: 70% of users experienced slow response times, and 30% couldn’t access our website at all. This caused a drop in successful transactions on the e-commerce platform.  
**Root Cause**: The root cause was a memory leak in the application server that led to the server running out of resources, making the web services unresponsive.

## Timeline

- **08:00 AM**: The issue was detected by an automated monitoring alert, showing high latency on the website.
- **08:05 AM**: I checked the alert and saw that memory usage on the application server had spiked.
- **08:10 AM**: I started investigating the web server configuration, thinking it might be a misconfiguration issue.
- **08:20 AM**: I couldn’t find any configuration issues, so I escalated it to the DevOps team.
- **08:30 AM**: The DevOps team looked into the database, thinking a slow query might be causing the problem.
- **08:45 AM**: After optimizing some database queries, the issue was still there.
- **09:00 AM**: We shifted focus to the application logs and found repeated errors from the session management service.
- **09:10 AM**: The memory leak in the session management service was identified as the root cause.
- **09:15 AM**: We restarted the application server to temporarily fix the issue while preparing a permanent solution.
- **09:30 AM**: The development team deployed a patch to fix the memory leak.
- **10:00 AM**: Everything was back to normal, and the services were fully restored.

## Root Cause and Resolution

The problem was a memory leak in the session management service of our application server. The leak happened because user sessions weren’t being cleaned up properly, so the server’s memory kept filling up until it couldn’t handle any more requests. This led to slow responses and service outages for a large number of users.

To fix it, we restarted the application server to clear the memory, which temporarily brought things back online. Then, we found and fixed the buggy code causing the memory leak and deployed a patch to prevent it from happening again.

## Corrective and Preventative Measures

To make sure this doesn’t happen again, here’s what we’ll do:

1. **Better Memory Monitoring**: We’ll improve monitoring of the application server’s memory usage and set up more detailed alerts to catch issues earlier.
   
2. **Stronger Code Review and Testing**: We’ll enforce more thorough code reviews and testing, especially around how memory is handled in the code.

3. **Automated Garbage Collection Checks**: We’ll use tools to automatically check how garbage collection is working during the testing phase to spot potential memory leaks.

4. **Action Items**:
   - [ ] Apply the memory leak fix to all production servers.
   - [ ] Set up real-time memory usage dashboards.
   - [ ] Hold a training session on memory management best practices.
   - [ ] Review the session management code to find and fix any other issues.

By taking these steps, we’ll reduce the chances of this happening again and make our services more reliable.
