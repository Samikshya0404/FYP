import { Injectable } from '@angular/core';
import { CanActivate ,ActivatedRouteSnapshot ,RouterStateSnapshot, Router  } from '@angular/router';
import { Observable } from 'rxjs';
// import { ToastrService } from 'ngx-toastr';
// import { NotifierService } from 'angular-notifier';
@Injectable({
  providedIn: 'root'
})
export class GuardsService implements CanActivate{

  constructor( private router: Router) { }

  canActivate(next: ActivatedRouteSnapshot, state: RouterStateSnapshot): Observable<boolean> | Promise<boolean> | boolean {
    if (localStorage.getItem('access_token')) {
        return true;
    }
    else {
    alert('please login to watch videos!!')
    this.router.navigate(['/login']);
    return false;
    }

  }
}
